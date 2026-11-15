import numpy as np

class ChaoticAttractorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] for better numerical stability
        x_normalized = x / 5.0
        
        # Radial component with multiple peaks
        r = np.sqrt(np.sum(x_normalized**2))
        radial = np.sin(5 * np.pi * r) * np.exp(-r**2 / 2)
        
        # Multi-modal sinusoidal terms
        modal = 0
        for i in range(self.dim):
            modal += np.sin(3 * np.pi * x_normalized[i]) * np.cos(2 * np.pi * x_normalized[i])
            
        # Periodic radial interaction
        periodic = 0
        for i in range(self.dim):
            periodic += np.sin(4 * np.pi * x_normalized[i]) * np.cos(4 * np.pi * x_normalized[i])
            
        # Gradient discontinuity using step functions
        discontinuity = 0
        for i in range(self.dim):
            discontinuity += np.abs(np.floor(x_normalized[i] * 2) - x_normalized[i] * 2)
            
        # Symmetry-breaking perturbation
        symmetry_break = 0
        for i in range(self.dim):
            symmetry_break += np.sin(x_normalized[i] * np.pi / 2) * np.cos(x_normalized[i] * np.pi / 3)
            
        # Combine all components
        result = 0.3 * radial + 0.25 * modal + 0.2 * periodic + 0.15 * discontinuity + 0.1 * symmetry_break
        
        # Add small random noise to increase problem difficulty
        noise = 0.01 * np.sum(np.sin(x_normalized * 11) * np.cos(x_normalized * 9))
        result += noise
        
        return result