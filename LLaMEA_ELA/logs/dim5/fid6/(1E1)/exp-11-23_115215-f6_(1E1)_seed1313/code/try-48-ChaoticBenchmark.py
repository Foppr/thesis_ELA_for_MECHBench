import numpy as np

class ChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic parameters
        self.r = 3.9  # Logistic map parameter
        self.sigma = 0.1
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f_val = np.sum(x**2)
        
        # Add chaotic logistic map components
        chaotic_sum = 0.0
        for i in range(self.dim):
            # Logistic map with input scaled to [0,1]
            scaled_x = (x[i] + 5.0) / 10.0
            chaotic_val = self.r * scaled_x * (1 - scaled_x)
            chaotic_sum += chaotic_val**2
            
        f_val += 0.5 * chaotic_sum
        
        # Add radial basis function components with random centers
        rbfs = 0.0
        for i in range(self.dim):
            # Radial basis with varying width and height
            center = np.sin(i) * 3.0  # Varying centers
            width = 0.5 + 0.5 * np.cos(i)
            height = 1.0 + 0.5 * np.sin(i)
            rbfs += height * np.exp(-0.5 * ((x[i] - center) / width)**2)
            
        f_val += 0.3 * rbfs
        
        # Add asymmetric coupling terms
        asym_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Asymmetric interaction based on direction
                diff = x[i] - x[j]
                asym_coupling += (0.1 * np.sin(diff) + 
                                0.05 * np.cos(2*diff) + 
                                0.03 * np.tan(0.5*diff))
                
        f_val += asym_coupling
        
        # Add a chaotic attractor component using sine-cosine combinations
        attractor = 0.0
        for i in range(self.dim):
            attractor += (np.sin(x[i]) * np.cos(2*x[i]) + 
                         np.cos(3*x[i]) * np.sin(0.5*x[i]) +
                         np.sin(4*x[i]) * np.cos(0.7*x[i]))
            
        f_val += 0.2 * attractor
        
        # Add a global scaling factor that depends on all dimensions
        global_factor = np.exp(-0.1 * np.sum(np.abs(x)))
        f_val *= (1.0 + global_factor)
        
        return f_val