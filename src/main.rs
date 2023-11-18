use std::fs;
use std::path::PathBuf;
use rocket::http::ContentType;
#[macro_use] extern crate rocket;

#[get("/")]
fn main_index() -> (ContentType, &'static str) {
    let html_content = fs::read_to_string("html/x1.html");
    (ContentType::HTML, Box::leak(html_content.expect("REASON").into_boxed_str()))
}

#[get("/signup")]
fn signup() -> (ContentType, &'static str) {
    let html_content = fs::read_to_string("html/signup.html");
    (ContentType::HTML, Box::leak(html_content.expect("REASON").into_boxed_str()))
}

//#[get("/design.css")]
//fn signup_css() -> (ContentType, &'static str) {
//    let html_content = fs::read_to_string("css/design.css");
//    (ContentType::CSS, Box::leak(html_content.expect("REASON").into_boxed_str()))
//}

#[get("/<file..>", rank = 1)]
fn css_files(file: PathBuf) -> (ContentType, &'static str) {
   println!("{}", file.display());
   let Some(extension) = file.extension() else { todo!() };
   if extension == "css" {
       let file_name = file.file_name().unwrap().to_str().unwrap();
        let css_content = fs::read_to_string("css/".to_owned() + file_name);
            return (ContentType::CSS, Box::leak(css_content.expect("REASON").into_boxed_str()));
   }  
   let file_name = file.file_name().unwrap().to_str().unwrap();
   let css_content = fs::read_to_string("js/".to_owned() + file_name).expect("REASON");
   println!("{}", css_content.as_str());
   (ContentType::JavaScript, Box::leak(css_content.into_boxed_str()))
}


#[launch]
fn rocket() -> _ {
    rocket::build().mount("/", routes![main_index, signup, css_files])
}

