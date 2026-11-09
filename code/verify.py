"""Read-only checks of the released numerical summaries; no simulation or fitting."""
import csv, hashlib, math, platform
from pathlib import Path
from collections import Counter, defaultdict

ROOT = Path(__file__).resolve().parent.parent
def read(name):
    with (ROOT / "data" / name).open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))
def close(a, b, label):
    if not math.isclose(float(a), float(b), rel_tol=1e-11, abs_tol=1e-13):
        raise AssertionError(f"{label}: {a} != {b}")
def quantile(x, p):
    x = sorted(x); z = (len(x)-1)*p; i = int(z); f = z-i
    return x[i]*(1-f) + x[min(i+1,len(x)-1)]*f
def main():
    with (ROOT / "SHA256SUMS.txt").open(encoding="utf-8") as f:
        for line in f:
            digest, name = line.rstrip("\n").split("  ", 1)
            path = ROOT / name
            if hashlib.sha256(path.read_bytes()).hexdigest() != digest:
                raise AssertionError(f"checksum mismatch: {name}")
    isolated, decisions = read("isolated_risk.csv"), read("decision_tension.csv")
    assert len(isolated)==160 and len(decisions)==40
    groups=defaultdict(list)
    for r in isolated: groups[(r["regime"],r["base_id"])].append(r)
    assert len(groups)==40 and all(len(v)==4 and {x["strategy_id"] for x in v}=={"S1","S2","S3","S4"} for v in groups.values())
    for r in decisions:
        rows=groups[(r["regime"],r["base_id"])]
        for model in ("D1","D0_LOG","D0_RAW"):
            ordered=sorted(rows,key=lambda x:(float(x[model+"_predicted_absolute_CVaR90"]),x["strategy_id"]))
            assert r[model+"_selected_schedule"]==ordered[0]["strategy_id"]
            close(r[model+"_best_vs_second_margin"],float(ordered[1][model+"_predicted_absolute_CVaR90"])-float(ordered[0][model+"_predicted_absolute_CVaR90"]),"selection margin")
        assert r["D1_selected_schedule"]==r["D0_LOG_selected_schedule"]==r["D0_RAW_selected_schedule"]
    triple=read("compound_111.csv"); pair=read("compound_pairwise.csv")
    assert len(triple)==160 and len(pair)==480
    data=defaultdict(list)
    for r in triple:
        r["cell"]="111"; data[(r["regime"],r["cell"])].append(r)
    for r in pair: data[(r["regime"],r["cell"])].append(r)
    metrics={}
    for r in read("metrics_111.csv"):
        metrics[(r["regime"],"111",r["model"])]=r
    for r in read("metrics_pairwise.csv"):
        metrics[(r["regime"],r["cell"],r["model"])]=r
    boots=defaultdict(list)
    for r in read("bootstrap_111.csv"): boots[(r["regime"],"111")].append(float(r["Q_boot"]))
    for r in read("bootstrap_pairwise.csv"): boots[(r["regime"],r["cell"])].append(float(r["Q_boot"]))
    table=read("transport_figure_table.csv"); assert len(table)==8 and len(data)==8
    for r in table:
        key=(r["severity"],r["cell"]); rows=data[key]; assert len(rows)==80 and len({x["base_id"] for x in rows})==20
        assert all(v==4 for v in Counter(x["base_id"] for x in rows).values())
        rmse={}
        for model in ("D1","D0_LOG","D0_RAW"):
            errors=[]
            for x in rows:
                obs=x["Y_obs_111"] if key[1]=="111" else x["Y_obs_cell"]
                err=float(x[model+"_predicted_Y"])-float(obs)
                close(err,x[model+"_error_pred_minus_obs"],"prediction error")
                errors.append(err)
            rmse[model]=math.sqrt(sum(e*e for e in errors)/len(errors))
            close(rmse[model],metrics[(*key,model)]["RMSE"],"metrics RMSE")
            close(rmse[model],r["RMSE_"+model],"figure RMSE")
        close(rmse["D1"]/rmse["D0_LOG"],r["Q"],"ratio")
        assert len(boots[key])==10000
        close(quantile(boots[key],.025),r["CI_low"],"lower CI")
        close(quantile(boots[key],.975),r["CI_high"],"upper CI")
        wins=sum(abs(float(x["D1_error_pred_minus_obs"]))<abs(float(x["D0_LOG_error_pred_minus_obs"])) for x in rows)
        assert wins==80
        print(*key, "D1 wins", wins, "/ 80; Q", r["Q"])
    support=read("support_111.csv")+read("support_pairwise.csv")
    assert len(support)==8
    for r in support:
        rows=data[(r["regime"],r["cell"])]
        col="X_log_111" if r["cell"]=="111" else "X_log_cell"
        x=[float(z[col]) for z in rows]; low=float(r["DEV_min"]); high=float(r["DEV_max"])
        close(min(x),r["predictor_min"],"support min"); close(max(x),r["predictor_max"],"support max")
        close(sum(v<low for v in x)/80,r["fraction_below_original_DEV_min"],"below DEV")
        close(sum(v>high for v in x)/80,r["fraction_above_original_DEV_max"],"above DEV")
    print("PASS: checksums, 40 absolute-score selections, eight RMSE/CI and support comparisons;", platform.python_version())
if __name__ == "__main__": main()
