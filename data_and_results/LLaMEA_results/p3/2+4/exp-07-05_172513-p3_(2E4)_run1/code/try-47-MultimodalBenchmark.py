import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Quadratic basin term for global attraction
        quadratic = np.sum(x_scaled**2)
        
        # Chaotic sinusoidal component with varying frequencies
        chaotic = np.sum(np.sin(10 * np.pi * x_scaled) * np.cos(7 * np.pi * x_scaled))
        
        # Exponential barrier terms to create rugged terrain with modified weights
        barriers = np.sum(1.8 * np.exp(-4 * np.abs(x_scaled)) * np.sin(3 * np.pi * x_scaled)**2)
        
        # Saddle point structure using mixed polynomial terms with cubic addition
        saddle = np.sum(x_scaled**4 - 2 * x_scaled**2 + 0.6 * x_scaled**3)
        
        # Add cross-dimensional coupling term with modified strength
        coupling = np.sum(x_scaled[:-1] * x_scaled[1:] * np.sin(5 * np.pi * x_scaled[:-1]) * 0.7)
        
        # Introduce additional high-frequency oscillation for increased complexity
        high_freq = np.sum(np.sin(15 * np.pi * x_scaled) * np.cos(12 * np.pi * x_scaled))
        
        # Add a quartic coupling term for enhanced multimodality
        quartic_coupling = np.sum((x_scaled[:-1]**2 + x_scaled[1:]**2) * np.sin(4 * np.pi * x_scaled[:-1]) * 0.5)
        
        # Combine all components with different weights
        return 0.5 * quadratic + 2.0 * chaotic + barriers + 0.3 * saddle + 0.1 * coupling + 0.8 * high_freq + 0.2 * quartic_coupling