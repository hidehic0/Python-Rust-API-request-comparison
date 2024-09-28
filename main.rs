use reqwest::Client;

type Result<T> = std::result::Result<T, Box<dyn std::error::Error>>;
#[tokio::main]
async fn main() -> Result<()> {
    let client = Client::new();
    let url = "https://pokeapi.co/api/v2/pokemon/987";
    let res = client.get(url).send().await?;

    let body = res.text().await?; // 3
    println!("{}", body);
    Ok(())
}
