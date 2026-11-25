import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Enhanced polynomial interaction terms with higher degree and modified coefficients
        f1 = np.sum(x_scaled**6) * 2.0
        
        # Chaotic exponential decay with sinusoidal modulation and increased frequency
        f2 = np.sum(np.exp(-0.5 * np.abs(x_scaled)) * np.sin(5 * np.pi * x_scaled) * np.cos(2 * np.pi * x_scaled))
        
        # Cross-terms with enhanced cosine interaction and radial barrier
        f3 = np.sum(np.cos(x_scaled[:-1] * x_scaled[1:]) * (1.0 + 0.5 * np.exp(-2.0 * (x_scaled[:-1]**2 + x_scaled[1:]**2))))
        
        # High-frequency oscillations with amplitude modulation
        f4 = np.sum(np.sin(15 * x_scaled) * np.cos(10 * x_scaled) * (1.0 + 0.3 * np.sin(7 * x_scaled)))
        
        # Modified Gaussian term with multiple peaks and enhanced conditioning
        f5 = np.sum(np.exp(-0.6 * x_scaled**2) * (1.0 + 0.4 * np.sin(4 * np.pi * x_scaled)))
        
        # Additional radial harmonic terms for increased complexity
        r = np.sqrt(np.sum(x_scaled**2))
        f6 = np.sum(np.sin(8 * r) * np.cos(6 * r) * (1.0 + 0.2 * np.sin(3 * r)))
        
        # Combined function with extreme curvature variations and multiple local minima
        return 2.5 * f1 + 0.7 * f2 + 0.4 * f3 + 0.3 * f4 + 0.35 * f5 + 0.2 * f6