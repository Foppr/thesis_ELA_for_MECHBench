import numpy as np

class SaddleMountainBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f1 = 0.5 * np.sum(x**2)
        
        # Add multiple asymmetric Gaussian peaks with varying heights and widths
        peaks = []
        for i in range(4):
            mu = np.array([2.0 * np.sin(0.5 * i), 3.0 * np.cos(0.3 * i)] + [0.0] * (self.dim - 2))[:self.dim]
            sigma = 0.3 + 0.4 * np.sin(0.7 * i)
            height = 1.5 + 2.0 * np.cos(0.4 * i)
            peak = height * np.exp(-0.5 * np.sum(((x - mu) / sigma)**2))
            peaks.append(peak)
        
        f2 = np.sum(peaks)
        
        # Add saddle point structure with hyperbolic tangent modulation
        f3 = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                f3 += np.tanh(x[i]) * np.tanh(x[j]) * np.sin(1.5 * x[i] * x[j])
        
        # Introduce gradient variation through fractional exponents
        f4 = 0.0
        for i in range(self.dim):
            f4 += np.abs(x[i])**1.8 * np.sin(2.5 * x[i])
        
        # Add asymmetric basin structure with exponential decay and cosine modulation
        f5 = 0.0
        for i in range(self.dim):
            f5 -= np.exp(-0.15 * (x[i] - 1.5)**2) * np.cos(0.6 * x[i])
        
        # Add cross-terms to increase interaction complexity
        f6 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f6 += 0.3 * np.sin(x[i] + x[j]) * np.cos(0.5 * x[i] * x[j])
        
        # Add a new component to improve robustness and challenge
        f7 = 0.0
        for i in range(self.dim):
            f7 += 0.2 * np.sin(3.0 * x[i]) * np.cos(0.5 * x[i]**2)
        
        # Add a new component to increase multimodality and complexity
        f8 = 0.0
        for i in range(self.dim):
            f8 += 0.1 * np.sin(0.5 * x[i]) * np.exp(-0.1 * x[i]**2)
        
        # Add a new component to enhance landscape complexity and challenge
        f9 = 0.0
        for i in range(self.dim):
            f9 += 0.15 * np.cos(2.0 * x[i]) * np.sin(0.3 * x[i]**3)
        
        # Add a new component to increase interaction between dimensions
        f10 = 0.0
        for i in range(self.dim):
            f10 += 0.05 * np.sin(1.2 * x[i]) * np.cos(1.8 * x[(i+1) % self.dim])
        
        # Add noise term to increase robustness
        noise = 0.02 * np.random.rand()
        
        # Combine all components
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 + noise