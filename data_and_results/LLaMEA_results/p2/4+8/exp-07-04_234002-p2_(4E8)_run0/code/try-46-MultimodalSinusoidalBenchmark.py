import numpy as np

class MultimodalSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Compute the multimodal function with chaotic sinusoidal components
        result = 0.0
        
        # Main chaotic sinusoidal contribution with fractal-like behavior
        for i in range(self.dim):
            # Add chaotic perturbations using fractional powers and nested trigonometric functions
            result += 1.3 * np.sin(2.0 * x[i]) * np.cos(1.3 * x[i]) * np.sin(0.8 * x[i]**1.5) + \
                      0.3 * x[i]**3 + 0.05 * x[i]**4 + 0.01 * x[i]**5
            
        # Add cross-dimensional coupling with fractal-like interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Introduce fractal-like coupling with multiple frequency interactions
                result += 0.08 * np.sin(3.0 * x[i]) * np.cos(1.5 * x[j]) * \
                          np.sin(0.5 * (x[i]**2 + x[j]**2)) + \
                          0.03 * x[i]**2.5 * x[j]**1.8
                
        # Add global scaling with chaotic polynomial terms
        x_squared = np.sum(x**2)
        x_fourth = np.sum(x**4)
        x_sixth = np.sum(x**6)
        x_eighth = np.sum(x**8)
        result = result * (1.0 + 0.4 * x_squared + 0.15 * x_fourth + 0.08 * x_sixth + 0.03 * x_eighth)
        
        # Add fractal-like Gaussian noise with varying scales
        noise = 0.002 * np.sum(np.exp(-0.5 * (x / 0.3)**2) * np.sin(5.0 * x))
        result += noise
        
        # Add a small chaotic perturbation term to increase landscape complexity
        chaotic_term = 0.005 * np.sum(np.sin(10.0 * x) * np.cos(7.0 * x))
        result += chaotic_term
        
        return result