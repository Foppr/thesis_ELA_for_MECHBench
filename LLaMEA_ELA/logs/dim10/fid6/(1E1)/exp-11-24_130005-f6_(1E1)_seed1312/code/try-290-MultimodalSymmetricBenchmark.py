import numpy as np

class MultimodalSymmetricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Radial component with multiple symmetric peaks
        r = np.sqrt(np.sum(x_scaled**2))
        radial = 1.0 + 0.5 * np.sin(5.0 * r) * np.cos(3.0 * r)
        
        # Trigonometric oscillations in each dimension
        trig_sum = 0.0
        for i in range(self.dim):
            trig_sum += np.sin(2.0 * x_scaled[i]) + 0.5 * np.cos(4.0 * x_scaled[i])
        
        # Cross-dimensional interaction terms with varying weights
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = 1.0 / (1.0 + abs(i - j))
                cross_term += weight * np.sin(x_scaled[i] * x_scaled[j]) * \
                             np.cos(x_scaled[i] + x_scaled[j])
        
        # Symmetric polynomial component
        poly = 0.0
        for i in range(self.dim):
            poly += (x_scaled[i]**4 - 2.0 * x_scaled[i]**2 + 1.0)
        
        # Gaussian peaks at symmetric positions
        gaussian = 0.0
        for i in range(self.dim):
            center = np.sin(i * np.pi / self.dim) * 0.5
            gaussian += np.exp(-5.0 * (x_scaled[i] - center)**2)
        
        # Combined function with adjusted weights
        return 1.5 * radial + 0.8 * trig_sum + 0.3 * cross_term + 0.4 * poly + 0.6 * gaussian