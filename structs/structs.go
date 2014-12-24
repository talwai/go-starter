package structs

import (
        "bytes"
        "fmt"
        "time"
)

type MessageType uint

var (
        ErrExecutingCommand = fmt.Errorf("Error executing Command")
        ErrNoClient = fmt.Errorf("Could not find client")
)

const (
        ConnectType MessageType = iota
        DisconnectType
        PingType
        PongType
        CommandType
        ResultType
)




