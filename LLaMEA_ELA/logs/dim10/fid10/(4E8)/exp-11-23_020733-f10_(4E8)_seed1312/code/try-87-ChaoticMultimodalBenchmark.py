import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters with enhanced sensitivity
        self.r = 3.995  # Slightly increased logistic map parameter for more chaos
        self.alpha = 1.5  # Increased asymmetry factor
        self.beta = 0.6   # Adjusted radial basis scaling
        self.gamma = 1.0  # Strengthened saddle point interaction
        
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
            chaotic_term += np.sin(chaotic_value * 20) * np.cos(chaotic_value * 13) + \
                           np.sin(chaotic_value * 9) * np.cos(chaotic_value * 5) + \
                           0.5 * np.sin(chaotic_value * 17)**2
        
        # Modified radial basis function component with multiple peaks and enhanced interaction
        rb_term = 0.0
        for i in range(self.dim):
            # Multi-peak radial basis with different scaling factors and interaction terms
            rb_term += self.beta * (np.exp(-0.5 * ((x[i] - 2.0)**2 + (x[i] + 2.0)**2)) + \
                                   0.4 * np.exp(-0.5 * ((x[i] - 1.5)**2 + (x[i] + 1.5)**2)) + \
                                   0.6 * np.exp(-0.5 * ((x[i] - 3.5)**2 + (x[i] + 3.5)**2)) + \
                                   0.3 * np.exp(-0.5 * ((x[i] - 0.5)**2 + (x[i] + 0.5)**2))) * \
                      (1 + self.alpha * np.sin(7 * x[i]) * np.cos(4 * x[i]))
            
        # Enhanced saddle point component with higher-order interactions and cubic terms
        saddle_term = 0.0
        for i in range(self.dim):
            # Create asymmetric saddle points with cubic, quartic, and quintic terms
            saddle_term += self.gamma * (np.abs(x[i])**5 - 4 * np.abs(x[i])**4 + 6 * np.abs(x[i])**3 - 4 * np.abs(x[i])**2 + x[i]) * \
                          np.cos(4 * x[i] + np.pi/8) + \
                          0.4 * (x[i]**6 - 3 * x[i]**5 + 3 * x[i]**4 - x[i]**3)
        
        # Combine all components with nonlinear interactions
        result = 1.0 * np.sum(x**2) + 0.8 * chaotic_term + 0.7 * rb_term + 0.9 * saddle_term
        
        # Add enhanced exponential barrier near boundaries with variable penalty
        barrier = 3.0 * np.sum(np.exp(25 * (np.abs(x) - 5.0)) + 0.6 * np.exp(15 * (np.abs(x) - 5.0)))
        result += barrier
        
        # Add multi-frequency noise term with chaotic characteristics
        noise = 0.07 * np.sum(np.sin(45 * x) + np.cos(30 * x) + np.sin(20 * x)**3 + np.cos(15 * x)**2)
        result += noise
        
        # Add a novel correlation penalty term between dimensions
        corr_penalty = 0.0
        for i in range(self.dim-1):
            corr_penalty += 0.3 * (x[i] - x[i+1])**2 * np.sin(x[i] + x[i+1]) + \
                          0.1 * (x[i] * x[i+1])**2 * np.cos(x[i] - x[i+1])
        result += corr_penalty
        
        # Final scaling to maintain balanced complexity
        result *= 1.7
        
        return result