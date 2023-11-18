use std::fs;
use rocket::http::ContentType;
#[macro_use] extern crate rocket;

#[get("/")]
fn main_index() -> (ContentType, &'static str) {
    let html_content = fs::read_to_string("x1.html");
    (ContentType::HTML, Box::leak(html_content.expect("REASON").into_boxed_str()))
}

#[get("/signup")]
fn signup() -> (ContentType, &'static str) {
    let html_content = fs::read_to_string("html/signup.html");
    (ContentType::HTML, Box::leak(html_content.expect("REASON").into_boxed_str()))
}

#[get("/design.css")]
fn signup_css() -> (ContentType, &'static str) {
    let html_content = fs::read_to_string("css/design.css");
    (ContentType::CSS, Box::leak(html_content.expect("REASON").into_boxed_str()))
}

#[launch]
fn rocket() -> _ {
    rocket::build().mount("/", routes![main_index, signup, signup_css])
}

