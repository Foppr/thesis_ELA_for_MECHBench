import numpy as np

class RadialChaoticOscillator:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Radial component with multi-scale Gaussian peaks
        for i in range(self.dim):
            # Radial basis functions with varying widths and heights
            radial_term = np.exp(-0.5 * (x[i] / 2.0)**2) * np.sin(10 * x[i])
            result += 0.3 * radial_term**2
        
        # Multi-frequency sinusoidal oscillations with adaptive amplitudes
        for i in range(self.dim):
            oscillation = (np.sin(5 * x[i]) + 
                          0.7 * np.sin(15 * x[i]) + 
                          0.4 * np.sin(45 * x[i]) + 
                          0.2 * np.sin(135 * x[i]))
            result += 0.4 * oscillation**2
        
        # Cross-dimensional coupling with radial dependency (modified strength)
        for i in range(self.dim - 1):
            # Coupling based on Euclidean distance between dimensions
            dist = np.sqrt((x[i] - x[i+1])**2 + 0.1)
            coupling = np.exp(-dist) * np.sin(10 * (x[i] + x[i+1]))  # Increased frequency
            result += 0.7 * coupling**2  # Increased coupling strength
        
        # Adaptive conditioning based on position and dimensionality
        position_norm = np.sum(x**2)
        conditioning = 1.0 + 0.5 * np.tanh(position_norm / self.dim)
        result *= conditioning
        
        # Chaotic modulation with time-like phase progression
        chaos_modulation = 0.0
        for i in range(self.dim):
            phase = x[i] * (1.0 + 0.3 * np.sin(x[i]**2))
            chaos_modulation += np.sin(7 * phase) * np.cos(4 * phase)
        result += 0.5 * chaos_modulation**2
        
        # Multi-scale harmonic structure with varying frequencies (added cubic terms)
        for i in range(self.dim):
            harmonic = (np.sin(3 * x[i]) + 
                       0.8 * np.sin(9 * x[i]) + 
                       0.6 * np.sin(27 * x[i]) + 
                       0.4 * np.sin(81 * x[i]))
            result += 0.25 * harmonic**3  # Increased weight on cubic terms
        
        # Add dimensionality-dependent scaling factor
        result *= (1.0 + 0.3 * np.log(self.dim + 1))
        
        # Final regularization with quartic terms
        result += 0.01 * np.sum(x**4) / self.dim
        
        return result