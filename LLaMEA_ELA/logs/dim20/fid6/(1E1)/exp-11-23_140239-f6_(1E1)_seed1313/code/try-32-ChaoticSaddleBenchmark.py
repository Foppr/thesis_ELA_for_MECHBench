import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = 0.1 * np.sum(x**2)
        
        # Add multiple chaotic saddle points with varying scales and adaptive weights
        for i in range(1, min(6, self.dim + 1)):  # Limit to 5 saddle points
            # Saddle point locations with exponential spacing and chaotic perturbation
            saddle_x = i * 0.5 * np.sin(i * 1.3) * (1 + 0.1 * np.sin(i * 2.7))
            saddle_y = i * 0.5 * np.cos(i * 1.3) * (1 + 0.1 * np.cos(i * 2.7))
            
            # Adaptive scaling based on dimension
            scale = 1.0 + 0.2 * np.log(i + 1)
            
            # Chaotic distance from saddle point with adaptive scaling
            if self.dim > 1:
                dist = np.sqrt(((x[0] - saddle_x) / scale)**2 + ((x[1] - saddle_y) / scale)**2)
                
                # Add chaotic influence with exponential decay and amplitude modulation
                amplitude = 5.0 * (1.0 + 0.3 * np.sin(i * 0.7))
                result += amplitude * np.exp(-dist**2 / (2 * (i * 0.1)**2)) * np.sin(dist * i)
        
        # Add higher-order polynomial terms for increased complexity
        for i in range(self.dim):
            result += 0.5 * x[i]**4 - 2 * x[i]**2
        
        # Add multi-modal structure with additional chaotic peaks
        multimodal = 0.0
        for i in range(1, min(4, self.dim + 1)):
            peak_x = 3.0 * np.sin(i * 1.5) + 0.5 * np.cos(i * 2.3)
            peak_y = 3.0 * np.cos(i * 1.5) + 0.5 * np.sin(i * 2.3)
            
            if self.dim > 1:
                dist = np.sqrt((x[0] - peak_x)**2 + (x[1] - peak_y)**2)
                multimodal += 3.0 * np.exp(-dist**2 / (2 * (0.5 * i)**2)) * np.cos(dist * i * 0.5)
        
        # Add noise component to increase ruggedness
        noise = 0.1 * np.sum(np.sin(10 * x))
        
        return result + multimodal + noise