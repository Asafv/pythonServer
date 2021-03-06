# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import proto.chat_pb2 as chat__pb2


class ChatServerStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.ChatStream = channel.unary_stream(
        '/grpc.ChatServer/ChatStream',
        request_serializer=chat__pb2.Empty.SerializeToString,
        response_deserializer=chat__pb2.Text.FromString,
        )
    self.SendText = channel.unary_unary(
        '/grpc.ChatServer/SendText',
        request_serializer=chat__pb2.Text.SerializeToString,
        response_deserializer=chat__pb2.Empty.FromString,
        )


class ChatServerServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def ChatStream(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SendText(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ChatServerServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'ChatStream': grpc.unary_stream_rpc_method_handler(
          servicer.ChatStream,
          request_deserializer=chat__pb2.Empty.FromString,
          response_serializer=chat__pb2.Text.SerializeToString,
      ),
      'SendText': grpc.unary_unary_rpc_method_handler(
          servicer.SendText,
          request_deserializer=chat__pb2.Text.FromString,
          response_serializer=chat__pb2.Empty.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'grpc.ChatServer', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
