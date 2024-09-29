#[warn(dead_code)]
use reqwest::Client;
use serde::Deserialize;
type Result<T> = std::result::Result<T, Box<dyn std::error::Error>>;

#[derive(Debug, Deserialize)]
struct StatName {
    name: String,
    url: String,
}

#[derive(Debug, Deserialize)]
struct Stat {
    base_stat: i32,
    effort: i32,
    stat: StatName,
}

#[tokio::main]
async fn main() -> Result<()> {
    let client = Client::new();
    let url = "https://pokeapi.co/api/v2/pokemon/987";
    let res = client.get(url).send().await?;

    let body = res.json::<Vec<Stat>>().await?; // 3
    println!("{}", body[0].base_stat);
    Ok(())
}
