package com.example.mlautogradecodetool.controller;

import java.io.IOException;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;
import com.example.mlautogradecodetool.model.JwtRequest;
import com.example.mlautogradecodetool.model.JwtResponse;
import com.example.mlautogradecodetool.model.User;
import com.example.mlautogradecodetool.service.UserService;

import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@Controller
public class UserController {

//    @Autowired
//    private UserService userService;
//
//    @GetMapping("/signup")
//    public String signup() {
//        return "signup";
//    }
//
//    @PostMapping("/signup")
//    public String signUp(@RequestBody User user, Model model) {
//        try {
//            userService.signUp(user);
//            return "redirect:/login"; // Redirect to login page after successful signup
//        } catch (Exception e) {
//            model.addAttribute("error", e.getMessage());
//            return "signup";
//        }
//    }
//
//    @GetMapping("/login")
//    public String login() {
//    	System.out.println("login with get");
//        return "login";
//    }
//
//
//    @PostMapping("/loginReq")
//    public String signIn(@RequestBody JwtRequest jwtRequest, HttpServletResponse response, Model model) {
//        try {
//            JwtResponse jwtResponse = userService.signIn(jwtRequest);
//            response.setHeader("Authorization", "Bearer " + jwtResponse.getToken());
//            // Redirect to home page upon successful login
//            System.out.println("token : "+jwtResponse.getToken());
//            System.out.println("login with post, redirected to home page");
//            return "redirect:/home";
//            
//        } catch (Exception e) {
//        	System.out.println("login with post, error occured");
//        	model.addAttribute("error", "Invalid credentials");
//        	return "login";
//
//        }
//    
//    }
//   
//    @GetMapping("/home")
//    public String home() {
//    	System.out.println("inside home page");
//        return "home";
//    }

    @Autowired
    private UserService userService;

    @GetMapping("/signup")
    public String signup(Model model) {
        model.addAttribute("user", new User());
        return "signup";
    }

    @PostMapping("/signup")
    public String signUp(@ModelAttribute User user, Model model) {
        try {
            userService.signUp(user);
            return "redirect:/login"; // Redirect to login page after successful signup
        } catch (Exception e) {
            model.addAttribute("error", e.getMessage());
            return "signup";
        }
    }

    @GetMapping("/login")
    public String login(Model model) {
        model.addAttribute("jwtRequest", new JwtRequest());
        return "login";
    }

    @PostMapping("/loginReq")
    public String signIn(@ModelAttribute JwtRequest jwtRequest, HttpServletResponse response, Model model) {
        try {
            JwtResponse jwtResponse = userService.signIn(jwtRequest);
            response.setHeader("Authorization", "Bearer " + jwtResponse.getToken());
//           Redirect to home page upon successful login
            return "redirect:/home";
            
            
        } catch (Exception e) {
            model.addAttribute("error", "Invalid credentials");
            return "login";
   
        }
    }

    @RequestMapping("/home")
public String homePage(Model model) {
    // Check if there are any flash attributes and add them to the model
    return "home";
}

}

