import numpy as np

class ChaoticRotationalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Quaternion-inspired rotational component with chaotic phase modulation
        rot_terms = []
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Chaotic rotational interaction with exponential barrier
                angle = np.arctan2(x_norm[j], x_norm[i])
                rot_term = np.sin(7 * angle + 3 * np.sin(13 * angle)) * np.exp(-2.0 * (x_norm[i]**2 + x_norm[j]**2))
                rot_terms.append(rot_term)
        
        # Multi-scale exponential decay landscape with chaotic modulation
        r = np.sqrt(np.sum(x_norm**2))
        exp_decay = np.sum(np.exp(-3.0 * (x_norm**2)) * np.sin(15 * x_norm) * np.cos(11 * x_norm))
        
        # Cross-dimensional resonance with non-linear coupling
        resonance = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.sin(5 * x_norm[i] * x_norm[j]) * np.exp(-0.5 * (x_norm[i]**2 + x_norm[j]**2))
                resonance += coupling
        
        # Chaotic sine-wave interference pattern with variable frequency
        interference = np.sum(np.sin(23 * x_norm + np.sin(41 * x_norm)) * np.exp(-0.3 * x_norm**2))
        
        # Multi-modal structure with rotational symmetry and phase shifts
        phase_shifts = np.linspace(0, 2*np.pi, self.dim, endpoint=False)
        symmetry_term = np.sum(np.sin(8 * r + phase_shifts) * np.exp(-0.4 * r**2))
        
        # Gradient discontinuity modifier with chaotic threshold
        discontinuity = 0.0
        for i in range(self.dim):
            if np.abs(x_norm[i]) > 0.3:
                discontinuity += np.sin(30 * x_norm[i]) * np.exp(-1.5 * x_norm[i]**2)
        
        # Combined function with chaotic weighting and complex interactions
        return (0.5 * np.sum(x_norm**4) + 0.3 * exp_decay + 0.2 * np.sum(rot_terms) + 
                0.15 * resonance + 0.1 * interference + 0.08 * symmetry_term + 0.05 * discontinuity)