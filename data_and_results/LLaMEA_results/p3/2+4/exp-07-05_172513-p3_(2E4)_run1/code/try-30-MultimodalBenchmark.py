import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Quadratic basin term for global attraction
        quadratic = np.sum(x_scaled**2)
        
        # Chaotic sinusoidal component with varying frequencies and amplitude modulation
        chaotic = np.sum(np.sin(12 * np.pi * x_scaled) * np.cos(8 * np.pi * x_scaled) * np.exp(-0.5 * x_scaled**2))
        
        # Enhanced exponential barrier terms with sharper transitions
        barriers = np.sum(np.exp(-3 * np.abs(x_scaled)) * (np.sin(4 * np.pi * x_scaled)**2 + 0.5 * np.cos(6 * np.pi * x_scaled)**2))
        
        # Saddle point structure with higher-order polynomial terms and cross-coupling
        saddle = np.sum(x_scaled**6 - 3 * x_scaled**4 + 2 * x_scaled**2)
        
        # Cross-dimensional coupling term to increase complexity
        coupling = np.sum(x_scaled[:-1] * x_scaled[1:] * np.sin(5 * np.pi * x_scaled[:-1]))
        
        # Combine all components with optimized weights
        return 0.3 * quadratic + 2.5 * chaotic + 2.0 * barriers + 0.4 * saddle + 0.2 * coupling