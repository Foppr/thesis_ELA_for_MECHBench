import numpy as np

class RadialOscillatoryFunction:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Base radial term with polynomial barrier
        r = np.sqrt(np.sum(x**2))
        result = r**4 / 4.0 + 0.5 * r**2
        
        # Sinusoidal oscillations in each dimension with varying frequencies
        for i in range(self.dim):
            result += 1.5 * np.sin(4.0 * x[i]) * np.cos(3.0 * x[i])
            
        # Cross-dimensional coupling with adaptive amplitudes based on dimension indices
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 1.0 / (1.0 + (i + j) * 0.05)
                result += coupling * np.sin(2.0 * x[i] + x[j]) * np.cos(x[i] - 2.0 * x[j])
                
        # Radial oscillation component with modified frequency
        result += 2.0 * np.sin(6.0 * r) * np.cos(4.0 * r)
        
        # Polynomial barrier terms with different exponents and exponential decay
        for i in range(self.dim):
            result += 0.5 * (x[i]**7 + x[i]**5) * np.exp(-abs(x[i]) / 2.0)
            
        # Additional high-frequency cross-dimensional interaction with modified scaling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.3 * np.sin(20.0 * x[i] * x[j]) * (1.0 / (i + j + 1)**0.6)
                
        # Central repulsion term with modified amplitude and frequency
        result += 1.2 * np.exp(-r**2 / 3.0) * np.sin(2.0 * r)
        
        # Additional dimension-dependent modulation to increase complexity
        for i in range(self.dim):
            result += 0.1 * x[i]**8 * np.cos(5.0 * x[i])
            
        return result