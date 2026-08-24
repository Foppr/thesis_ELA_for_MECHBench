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
        for i in range(5):  # Increased number of peaks
            mu = np.array([2.0 * np.sin(0.6 * i), 3.0 * np.cos(0.4 * i)] + [0.0] * (self.dim - 2))[:self.dim]
            sigma = 0.2 + 0.5 * np.sin(0.8 * i)  # Changed sigma range
            height = 1.0 + 2.5 * np.cos(0.5 * i)  # Changed height range
            peak = height * np.exp(-0.5 * np.sum(((x - mu) / sigma)**2))
            peaks.append(peak)
        
        f2 = np.sum(peaks)
        
        # Add saddle point structure with enhanced hyperbolic tangent modulation
        f3 = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):  # Reduced interaction range
                f3 += np.tanh(1.5 * x[i]) * np.tanh(1.2 * x[j]) * np.sin(2.0 * x[i] * x[j])  # Changed coefficients
        
        # Introduce gradient variation through fractional exponents
        f4 = 0.0
        for i in range(self.dim):
            f4 += np.abs(x[i])**1.9 * np.sin(3.0 * x[i])  # Increased exponent
        
        # Add asymmetric basin structure with exponential decay and cosine modulation
        f5 = 0.0
        for i in range(self.dim):
            f5 -= np.exp(-0.2 * (x[i] - 1.2)**2) * np.cos(0.7 * x[i])  # Changed parameters
        
        # Add cross-terms to increase interaction complexity
        f6 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f6 += 0.4 * np.sin(x[i] + x[j]) * np.cos(0.6 * x[i] * x[j])  # Increased coefficient
        
        # Add a new component to improve robustness and challenge
        f7 = 0.0
        for i in range(self.dim):
            f7 += 0.25 * np.sin(3.5 * x[i]) * np.cos(0.6 * x[i]**2)  # Changed coefficients
        
        # Add a new component to increase multimodality and complexity
        f8 = 0.0
        for i in range(self.dim):
            f8 += 0.15 * np.sin(0.6 * x[i]) * np.exp(-0.12 * x[i]**2)  # Changed coefficients
        
        # Add noise term to increase robustness
        noise = 0.025 * np.random.rand()  # Increased noise level
        
        # Combine all components
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + noise