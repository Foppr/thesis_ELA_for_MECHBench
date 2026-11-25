import numpy as np

class SpiralAttractorLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] for stability
        x_scaled = x / 5.0
        
        # Base radial component with spiral structure
        r = np.sqrt(np.sum(x_scaled**2))
        
        # Sine-cosine periodic interactions with varying frequencies
        periodic = np.sum(np.sin(3 * np.pi * x_scaled) * np.cos(4 * np.pi * x_scaled) + 
                         0.5 * np.sin(7 * np.pi * x_scaled) * np.cos(6 * np.pi * x_scaled) + 
                         0.3 * np.sin(11 * np.pi * x_scaled) * np.cos(9 * np.pi * x_scaled))
        
        # Spiral-like attraction terms with radial dependence
        spiral_attraction = np.sum(np.sin(2 * np.pi * r) * np.cos(3 * np.pi * r) * 
                                 (x_scaled[:-1]**2 + x_scaled[1:]**2))
        
        # Adaptive dimensionality scaling based on position
        dim_scaling = np.sum((1 + 0.5 * np.sin(5 * np.pi * x_scaled)) * x_scaled**2)
        
        # Embedded multi-spiral structure with phase shifts
        multi_spiral = np.sum(np.sin(8 * np.pi * r + 0.5 * np.pi * x_scaled) * 
                            np.cos(7 * np.pi * r + 0.3 * np.pi * x_scaled))
        
        # Cross-dimensional coupling with spiral geometry
        cross_coupling = np.sum((x_scaled[:-1] * x_scaled[1:] + 
                               0.5 * (x_scaled[:-1]**2 + x_scaled[1:]**2)) * 
                              np.sin(4 * np.pi * (x_scaled[:-1] - x_scaled[1:])))
        
        # Multi-modal component with embedded local minima
        multimodal = np.sum(np.sin(2 * np.pi * x_scaled)**2 + 
                          0.3 * np.sin(5 * np.pi * x_scaled)**3 + 
                          0.1 * np.sin(9 * np.pi * x_scaled)**4)
        
        # Radial harmonic component with multiple peaks
        radial_harmonic = np.sum(np.cos(6 * np.pi * r) + 0.7 * np.cos(12 * np.pi * r) + 
                               0.3 * np.cos(18 * np.pi * r))
        
        # Adaptive coupling with dynamic weights
        adaptive_coupling = np.sum((x_scaled[:-1] + x_scaled[1:])**2 * 
                                 np.sin(2.5 * np.pi * (x_scaled[:-1] - x_scaled[1:]) + 
                                        0.3 * r))
        
        # Embedded lattice structure with periodic boundaries
        lattice_structure = np.sum(np.sin(4 * np.pi * x_scaled) * np.cos(4 * np.pi * x_scaled) + 
                                 0.6 * np.sin(8 * np.pi * x_scaled) * np.cos(8 * np.pi * x_scaled))
        
        # Combined landscape with weighted components
        return (0.3 * periodic + 0.2 * spiral_attraction + 0.15 * dim_scaling + 
                0.12 * multi_spiral + 0.1 * cross_coupling + 0.08 * multimodal + 
                0.07 * radial_harmonic + 0.05 * adaptive_coupling + 0.03 * lattice_structure)