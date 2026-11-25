import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters with enhanced sensitivity
        self.r = 3.999  # Slightly increased logistic map parameter for more chaos
        self.alpha = 1.8  # Increased asymmetry factor
        self.beta = 0.7   # Adjusted radial basis scaling
        self.gamma = 1.2  # Strengthened saddle point interaction
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic component with higher-order interactions
        chaotic_term = 0.0
        for i in range(self.dim):
            # Generate chaotic sequence using logistic map with higher-order chaos
            if i == 0:
                x_prev = 0.5  # Initial value
            else:
                x_prev = x[i-1] if i < len(x) else 0.5
                
            # Logistic map iteration with higher-order chaos
            chaotic_value = self.r * x_prev * (1 - x_prev)
            chaotic_term += np.sin(chaotic_value * 25) * np.cos(chaotic_value * 17) + \
                           np.sin(chaotic_value * 11) * np.cos(chaotic_value * 7) + \
                           0.6 * np.sin(chaotic_value * 19)**2
        
        # Modified radial basis function component with multiple peaks and enhanced interaction
        rb_term = 0.0
        for i in range(self.dim):
            # Multi-peak radial basis with different scaling factors and interaction terms
            rb_term += self.beta * (np.exp(-0.5 * ((x[i] - 2.0)**2 + (x[i] + 2.0)**2)) + \
                                   0.4 * np.exp(-0.5 * ((x[i] - 1.5)**2 + (x[i] + 1.5)**2)) + \
                                   0.6 * np.exp(-0.5 * ((x[i] - 3.5)**2 + (x[i] + 3.5)**2)) + \
                                   0.3 * np.exp(-0.5 * ((x[i] - 0.5)**2 + (x[i] + 0.5)**2))) * \
                      (1 + self.alpha * np.sin(9 * x[i]) * np.cos(5 * x[i]))
            
        # Enhanced saddle point component with higher-order interactions and cubic terms
        saddle_term = 0.0
        for i in range(self.dim):
            # Create asymmetric saddle points with cubic, quartic, and quintic terms
            saddle_term += self.gamma * (np.abs(x[i])**5 - 4 * np.abs(x[i])**4 + 6 * np.abs(x[i])**3 - 4 * np.abs(x[i])**2 + x[i]) * \
                          np.cos(5 * x[i] + np.pi/6) + \
                          0.5 * (x[i]**6 - 3 * x[i]**5 + 3 * x[i]**4 - x[i]**3)
        
        # Combine all components with nonlinear interactions
        result = 1.2 * np.sum(x**2) + 0.9 * chaotic_term + 0.8 * rb_term + 1.0 * saddle_term
        
        # Add enhanced exponential barrier near boundaries with variable penalty
        barrier = 3.5 * np.sum(np.exp(30 * (np.abs(x) - 5.0)) + 0.7 * np.exp(20 * (np.abs(x) - 5.0)))
        result += barrier
        
        # Add multi-frequency noise term with chaotic characteristics
        noise = 0.08 * np.sum(np.sin(50 * x) + np.cos(35 * x) + np.sin(25 * x)**3 + np.cos(20 * x)**2)
        result += noise
        
        # Add a novel correlation penalty term between dimensions
        corr_penalty = 0.0
        for i in range(self.dim-1):
            corr_penalty += 0.35 * (x[i] - x[i+1])**2 * np.sin(x[i] + x[i+1]) + \
                          0.15 * (x[i] * x[i+1])**2 * np.cos(x[i] - x[i+1])
        result += corr_penalty
        
        # Final scaling to maintain balanced complexity
        result *= 1.8
        
        return result