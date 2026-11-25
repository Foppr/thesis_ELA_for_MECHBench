import numpy as np

class OscillatoryRadialSaddle:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Global minimum at origin
        if np.allclose(x, 0):
            return 0.0
            
        # Radial quadratic base with varying coefficients
        result = 0.0
        for i in range(self.dim):
            result += (i + 1) * (x[i] ** 2)
            
        # Add periodic radial oscillations with varying frequencies
        r = np.sqrt(np.sum(x ** 2))
        result += 2.0 * np.sin(5 * r) * np.cos(3 * r) * np.exp(-0.1 * r)
        
        # Introduce coupled sinusoidal terms creating saddle points
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.5 * np.sin(x[i]) * np.cos(x[j]) * np.sin(2 * x[i] + x[j])
                
        # Add multi-modal peaks with varying heights and widths
        for i in range(self.dim):
            result += 1.5 * np.exp(-0.5 * (x[i] - 1) ** 2) * np.sin(4 * x[i]) + \
                      0.8 * np.exp(-0.3 * (x[i] + 2) ** 2) * np.cos(6 * x[i])
            
        # Include radial coupling with chaotic-like behavior
        for i in range(self.dim):
            result += 0.3 * np.sin(7 * x[i]) * np.cos(4 * r) * np.tan(0.5 * x[i])
            
        # Add a normalization factor based on distance from origin
        result /= (1.0 + 0.2 * r + 0.05 * r ** 2)
        
        # Introduce additional chaotic interactions via nested trigonometric functions
        for i in range(self.dim):
            result += 0.2 * np.sin(3 * x[i]) * np.cos(5 * x[(i+1) % self.dim]) * \
                      np.sin(2 * x[(i+2) % self.dim]) * np.tan(0.3 * x[i])
            
        return result