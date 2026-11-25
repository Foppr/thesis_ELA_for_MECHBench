import numpy as np

class HybridMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Gaussian radial basis functions with varying widths and centers
        rbfs = 0.0
        centers = np.linspace(-4.5, 4.5, min(10, self.dim))
        widths = np.logspace(-1, 1, min(10, self.dim))
        
        for i in range(min(10, self.dim)):
            center = centers[i] if i < len(centers) else x[np.random.randint(0, self.dim)] if self.dim > 1 else 0.0
            width = widths[i] if i < len(widths) else np.random.uniform(0.5, 2.0)
            rbfs += np.exp(-0.5 * np.sum(((x - center) / width) ** 2))
        
        # Polynomial chaos expansion with Hermite polynomials
        chaos = 0.0
        for i in range(self.dim):
            # Use Hermite polynomial of degree 3
            h1 = x[i]
            h2 = x[i]**2 - 1
            h3 = x[i]**3 - 3*x[i]
            chaos += h1 + 0.5*h2 + 0.3*h3
        
        # Sine-wave interference patterns with frequency modulation
        interference = 0.0
        for i in range(self.dim):
            freq = 2.0 + 0.5 * np.sin(0.3 * x[i])
            for j in range(i+1, self.dim):
                dist = np.abs(x[i] - x[j])
                interference += np.sin(freq * dist) * np.cos(0.7 * dist) * np.exp(-0.1 * dist)
        
        # Asymmetric polynomial landscape with mixed monotonicity
        poly_landscape = 0.0
        for i in range(self.dim):
            if x[i] < 0:
                poly_landscape += 0.5 * x[i]**3 + 0.2 * x[i]**5
            else:
                poly_landscape += 0.3 * x[i]**4 - 0.1 * x[i]**6
        
        # Cross-term coupling with dynamic weights based on position
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = np.exp(-0.5 * (x[i]**2 + x[j]**2)) * (1.0 + 0.3 * np.sin(x[i] + x[j]))
                coupling += weight * np.sin(2.0 * x[i]) * np.cos(1.5 * x[j])
        
        # Add noise component for additional complexity
        noise = 0.05 * np.random.rand()
        
        # Combine all components with dynamic weights
        total = 0.4 * rbfs + 0.3 * chaos + 0.2 * interference + 0.08 * poly_landscape + 0.02 * coupling + noise
        
        return total