use hyper::{Request, Response, Body, Server};
use hyper::service::{make_service_fn, service_fn};
use std::net::{TcpListener, SocketAddr};

async fn handle_request(_req: Request<Body>) -> Result<Response<Body>, hyper::Error> {
    Ok(Response::new(Body::from("Hello from Rust!")))
}

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error + Send + Sync>> {
    let addr: SocketAddr = ([0, 0, 0, 0], 8081).into();

    let std_listener = TcpListener::bind(&addr)?;
    std_listener.set_nonblocking(true)?;

    println!("Starting Rust service on http://{}", addr);

    let make_svc = make_service_fn(|_conn| async {
        Ok::<_, hyper::Error>(service_fn(handle_request))
    });

    let server = Server::from_tcp(std_listener)?.serve(make_svc);

    server.await?;

    Ok(())
}

