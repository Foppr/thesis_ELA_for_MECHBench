import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters
        self.r = 3.95  # Logistic map parameter
        self.alpha = 0.8  # Asymmetry factor
        self.beta = 0.3   # Radial basis scaling
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Logistic map chaotic component
        chaotic_term = 0.0
        for i in range(self.dim):
            # Generate chaotic sequence using logistic map
            if i == 0:
                x_prev = 0.5  # Initial value
            else:
                x_prev = x[i-1] if i < len(x) else 0.5
                
            # Logistic map iteration
            chaotic_value = self.r * x_prev * (1 - x_prev)
            chaotic_term += np.sin(chaotic_value * 10) * np.cos(chaotic_value * 7)
        
        # Radial basis function component with asymmetric saddle points
        rb_term = 0.0
        for i in range(self.dim):
            # Asymmetric radial basis with different scaling factors
            rb_term += self.beta * np.exp(-0.5 * ((x[i] - 2.0)**2 + (x[i] + 2.0)**2)) * \
                      (1 + self.alpha * np.sin(3 * x[i]))
            
        # Saddle point component with multiple valleys
        saddle_term = 0.0
        for i in range(self.dim):
            # Create asymmetric saddle points using different exponents
            saddle_term += 0.5 * (np.abs(x[i])**3 - 2 * np.abs(x[i])**2 + x[i]) * \
                          np.cos(2 * x[i] + np.pi/4)
        
        # Combine all components with nonlinear interactions
        result = 0.8 * np.sum(x**2) + 0.5 * chaotic_term + 0.3 * rb_term + 0.4 * saddle_term
        
        # Add exponential barrier near boundaries to increase difficulty
        barrier = 1.5 * np.sum(np.exp(15 * (np.abs(x) - 5.0)))
        result += barrier
        
        # Add noise term with chaotic frequency components
        noise = 0.02 * np.sum(np.sin(30 * x) + np.cos(20 * x) + np.sin(15 * x)**2)
        result += noise
        
        # Final scaling to maintain balanced complexity
        result *= 1.2
        
        return result