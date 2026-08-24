import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Quadratic base term for global convergence
        f1 = np.sum(x**2)
        
        # Enhanced chaotic sine-wave interactions with higher frequency components and fractional exponents
        f2 = 0.6 * np.sum(np.sin(12.0 * x + np.sin(8.0 * x)) * np.cos(15.0 * x + np.sin(7.0 * x)) * np.sin(4.0 * np.sqrt(np.abs(x))))
        
        # Modified radial gradient with Gaussian-like decay, additional sinusoidal modulation, and fractional powers
        f3 = 0.4 * np.sum(np.exp(-0.5 * np.sum(x**2)) * np.sin(8.0 * np.sum(x**2)) * np.cos(4.0 * np.sum(x**2)) * np.sqrt(np.abs(np.sum(x**2))))
        
        # Cross-term interactions with cubic, quartic, and quintic polynomial modulation, plus chaotic coupling
        f4 = 0.3 * np.sum((x**3 + 0.7 * x**4 + 0.3 * x**5) * np.sin(10.0 * x) * np.cos(6.0 * x) * np.sin(3.0 * np.sqrt(np.abs(x))))
        
        # Multi-scale sinusoidal modulation with varying amplitudes, frequencies, and fractional components
        f5 = 0.3 * np.sum(np.sin(20.0 * x) * np.sin(25.0 * x) * np.cos(10.0 * x) * np.sin(5.0 * x) * np.cos(2.0 * np.sqrt(np.abs(x))))
        
        # Adaptive scaling with exponential, polynomial, and fractional components
        f6 = 0.2 * np.sum(np.exp(-0.2 * np.sum(x**2)) * (x**4 + 0.5 * x**5 + 0.2 * x**6) * np.sqrt(np.abs(x)))
        
        # Additional chaotic component with fractional powers, exponential decay, and multi-dimensional coupling
        f7 = 0.1 * np.sum(np.sin(np.sqrt(np.abs(x))) * np.cos(np.sqrt(np.abs(x))) * np.exp(-0.7 * np.sum(x**2)) * np.sin(3.0 * np.sum(x**2)))
        
        # Fractional polynomial coupling term for increased complexity and nonlinearity
        f8 = 0.15 * np.sum((x**2.5 + 0.4 * x**3.5) * np.cos(8.0 * x) * np.sin(5.0 * x) * np.exp(-0.3 * np.sum(x**2)))
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8