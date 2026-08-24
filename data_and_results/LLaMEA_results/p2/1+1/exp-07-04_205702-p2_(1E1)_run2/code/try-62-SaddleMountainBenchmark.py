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
            height = 2.0 + 1.5 * np.cos(0.4 * i)  # Slightly increased base height
            peak = height * np.exp(-0.5 * np.sum(((x - mu) / sigma)**2))
            peaks.append(peak)
        
        f2 = np.sum(peaks)
        
        # Add saddle point structure with hyperbolic tangent modulation
        f3 = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                f3 += np.tanh(x[i]) * np.tanh(x[j]) * np.sin(1.5 * x[i] * x[j])
        
        # Introduce gradient variation through fractional exponents (slightly altered)
        f4 = 0.0
        for i in range(self.dim):
            f4 += np.abs(x[i])**1.9 * np.sin(2.7 * x[i])  # Increased exponent and frequency
        
        # Add asymmetric basin structure with exponential decay and cosine modulation
        f5 = 0.0
        for i in range(self.dim):
            f5 -= np.exp(-0.18 * (x[i] - 1.7)**2) * np.cos(0.7 * x[i])  # Slight shift and scaling
        
        # Add cross-terms to increase interaction complexity (more terms added)
        f6 = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):  # Reduced interaction range
                f6 += 0.4 * np.sin(x[i] + x[j]) * np.cos(0.6 * x[i] * x[j])
        
        # Add additional high-order interaction terms for increased complexity
        f7 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                for k in range(j+1, self.dim):
                    f7 += 0.1 * np.sin(x[i] * x[j] * x[k]) * np.cos(0.3 * (x[i] + x[j] + x[k]))
        
        # Combine all components
        return f1 + f2 + f3 + f4 + f5 + f6 + f7