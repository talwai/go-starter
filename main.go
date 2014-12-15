package main

import (
    "net/http"
    "log"
)

type saySomethingHandler struct {
    whatToSay string
}

func (h *saySomethingHandler) ServeHTTP(w http.ResponseWriter, req *http.Request) {
    w.Write([]byte(h.whatToSay))
}

func main() {
    mux := http.NewServeMux()

    rh := http.RedirectHandler("http://www.google.com", 307)
    mux.Handle("/foo", rh)
    //mux.Handle requires an explicit http.Handler() object
    sh := &saySomethingHandler{whatToSay: "hello"}
    mux.Handle("/hello", sh)

    log.Printf("Listening on 8080")
    err := http.ListenAndServe(":8080", mux)
    if err != nil {
        log.Fatal("ListenAndServe: ", err)
    }
}
