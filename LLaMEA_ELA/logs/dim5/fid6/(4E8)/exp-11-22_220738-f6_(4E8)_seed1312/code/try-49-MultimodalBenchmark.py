import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with chaotic scaling
        f_val = np.sum(x**2) * (1.0 + 0.1 * np.sin(10.0 * np.sum(x**2)))
        
        # Chaotic oscillatory component with exponential decay
        for i in range(self.dim):
            f_val += 0.5 * np.sin(25.0 * x[i]) * np.exp(-0.15 * abs(x[i]))
            
        # Implicit constraint landscape with repulsion fields (modified)
        repulsion = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = abs(x[i] - x[j])
                repulsion += 1.0 / (1.0 + np.exp(6.0 * (dist - 1.5)))
        f_val += 0.4 * repulsion
        
        # Dynamic dimensional coupling with sine modulation (modified frequency)
        coupling = 0.0
        for i in range(self.dim - 1):
            coupling += x[i] * x[i+1] * np.sin(0.7 * (x[i]**2 + x[i+1]**2))
        f_val += 0.25 * coupling
        
        # Multiple Gaussian peaks with dynamic positions and widths (shifted)
        peak_count = min(5, self.dim // 2)
        for i in range(peak_count):
            idx = (i * 4) % self.dim
            if idx + 2 < self.dim:
                pos = np.array([x[idx], x[idx+1], x[idx+2]])
                center = np.array([0.5, -1.5, 1.0])
                width = 0.3 + 0.4 * np.sin(i * 0.5)
                f_val += 0.5 * np.exp(-0.5 * np.sum(((pos - center) / width)**2))
                
        # Exponential barrier terms to encourage boundary exploration (modified)
        barrier = 0.0
        for i in range(self.dim):
            barrier += np.exp(2.5 * (5.0 - abs(x[i])))
        f_val += 0.15 * barrier
        
        return f_val