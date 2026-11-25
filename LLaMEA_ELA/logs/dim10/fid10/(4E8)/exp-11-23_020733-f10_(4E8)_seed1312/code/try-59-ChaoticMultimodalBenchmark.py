import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters
        self.r = 3.99  # Logistic map parameter
        self.alpha = 1.2  # Asymmetry factor
        self.beta = 0.5   # Radial basis scaling
        self.gamma = 0.8  # Saddle point interaction strength
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Logistic map chaotic component with higher frequency interactions
        chaotic_term = 0.0
        for i in range(self.dim):
            # Generate chaotic sequence using logistic map
            if i == 0:
                x_prev = 0.5  # Initial value
            else:
                x_prev = x[i-1] if i < len(x) else 0.5
                
            # Logistic map iteration with higher sensitivity
            chaotic_value = self.r * x_prev * (1 - x_prev)
            chaotic_term += np.sin(chaotic_value * 15) * np.cos(chaotic_value * 11) + \
                           np.sin(chaotic_value * 7) * np.cos(chaotic_value * 3)
        
        # Enhanced radial basis function component with multiple peaks
        rb_term = 0.0
        for i in range(self.dim):
            # Multi-peak radial basis with different scaling factors
            rb_term += self.beta * (np.exp(-0.5 * ((x[i] - 2.5)**2 + (x[i] + 2.5)**2)) + \
                                   0.3 * np.exp(-0.5 * ((x[i] - 1.0)**2 + (x[i] + 1.0)**2)) + \
                                   0.5 * np.exp(-0.5 * ((x[i] - 3.0)**2 + (x[i] + 3.0)**2))) * \
                      (1 + self.alpha * np.sin(5 * x[i]))
            
        # Enhanced saddle point component with higher-order interactions
        saddle_term = 0.0
        for i in range(self.dim):
            # Create asymmetric saddle points with cubic and quartic terms
            saddle_term += self.gamma * (np.abs(x[i])**4 - 3 * np.abs(x[i])**3 + 2 * np.abs(x[i])**2 - x[i]) * \
                          np.cos(3 * x[i] + np.pi/6) + \
                          0.3 * (x[i]**5 - 2 * x[i]**4 + x[i]**3)
        
        # Combine all components with nonlinear interactions
        result = 1.2 * np.sum(x**2) + 0.7 * chaotic_term + 0.6 * rb_term + 0.8 * saddle_term
        
        # Add enhanced exponential barrier near boundaries with variable penalty
        barrier = 2.0 * np.sum(np.exp(20 * (np.abs(x) - 5.0)) + 0.5 * np.exp(10 * (np.abs(x) - 5.0)))
        result += barrier
        
        # Add multi-frequency noise term with chaotic characteristics
        noise = 0.05 * np.sum(np.sin(40 * x) + np.cos(25 * x) + np.sin(18 * x)**3 + np.cos(12 * x)**2)
        result += noise
        
        # Add a novel correlation penalty term between dimensions
        corr_penalty = 0.0
        for i in range(self.dim-1):
            corr_penalty += 0.2 * (x[i] - x[i+1])**2 * np.sin(x[i] + x[i+1])
        result += corr_penalty
        
        # Final scaling to maintain balanced complexity
        result *= 1.5
        
        return result