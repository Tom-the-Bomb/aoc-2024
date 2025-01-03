use std::{
    env,
    time::Instant,
    process::Command,
};

fn run_bin_day(day: u8) -> Option<String> {
    let cmd = Command::new("cargo")
        .args(["run", "--release", "--bin", &format!("day{day}")])
        .output()
        .unwrap();
    let stdout = String::from_utf8(cmd.stdout)
        .unwrap();
    let stderr = String::from_utf8(cmd.stderr)
        .unwrap();
    match (stdout.is_empty(), stderr.is_empty()) {
        (false, true) => Some(stdout),
        (false, false) => Some(format!("{stdout}{stderr}")),
        (true, _) => None,
    }
}

#[allow(clippy::option_if_let_else)]
fn main() {
    if let Some(day) = env::args()
        .collect::<Vec<String>>()
        .get(1)
        .and_then(|x| x.parse::<u8>().ok())
    {
        println!("{}",
            run_bin_day(day)
                .unwrap_or_else(|| format!("Solution does not exist yet for day {day}"))
        );
    } else {
        let mut day = 1;
        let instant = Instant::now();

        while let Some(output) = run_bin_day(day) {
            println!("{output}");
            day += 1;
        }
        let text = format!(
            "[Total Execution time: {:?}]",
            instant.elapsed(),
        );
        println!(
            "{text}\n{}",
            "=".repeat(text.chars().count())
        );
    }
}