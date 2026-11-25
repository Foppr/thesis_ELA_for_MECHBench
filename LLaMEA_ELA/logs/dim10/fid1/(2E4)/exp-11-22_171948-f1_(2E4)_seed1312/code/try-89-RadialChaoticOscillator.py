import numpy as np

class RadialChaoticOscillator:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Enhanced radial component with chaotic frequency modulation
        r = np.sqrt(np.sum(x**2))
        radial_term = (np.sin(15 * r) + 
                      0.6 * np.sin(45 * r) + 
                      0.3 * np.sin(120 * r) + 
                      0.1 * np.sin(200 * r))
        result += 3.0 * radial_term**2
        
        # Angular components with chaotic coupling and phase shifts
        for i in range(self.dim):
            angular = 0.0
            for j in range(i+1, self.dim):
                angle_diff = x[i] - x[j]
                phase_shift = np.sin(0.5 * (i + j)) * np.cos(0.3 * (i - j))
                angular += np.sin(7 * angle_diff + phase_shift) * np.cos(4 * angle_diff + phase_shift)
            result += 0.8 * angular**2
        
        # Multi-modal harmonic landscape with chaotic amplitude modulation
        for i in range(self.dim):
            # Chaotic amplitude modulation based on position
            amp_mod = 1.0 + 0.5 * np.sin(10 * x[i]) * np.cos(7 * x[i])
            harmonic = (amp_mod * np.sin(25 * x[i]) + 
                       0.8 * amp_mod * np.sin(75 * x[i]) + 
                       0.4 * amp_mod * np.sin(200 * x[i]) + 
                       0.2 * amp_mod * np.sin(500 * x[i]))
            result += 1.5 * harmonic**2
        
        # Dynamic conditioning with chaotic scaling
        conditioning = 1.0 + 1.2 * np.exp(-0.15 * r**2) * np.sin(3 * r)
        result *= conditioning
        
        # Enhanced cross-dimensional coupling with chaotic dependence
        for i in range(self.dim - 1):
            coupling = (np.sin(9 * (x[i] + x[i+1])) * 
                       np.cos(5 * (x[i] - x[i+1])) * 
                       np.sin(2 * r))
            result += 1.2 * coupling * (1.0 + 0.4 * r)
        
        # Stronger noise-like perturbations with chaotic radial dependency
        noise = 0.0
        for i in range(self.dim):
            phase_mod = np.sin(0.4 * i) * np.cos(0.3 * i)
            noise += (np.sin(30 * x[i] + i * 0.5 + phase_mod) * 
                     np.cos(20 * x[i] + i * 0.6 + phase_mod))
        result += 1.0 * noise * (1.0 + 0.4 * r)
        
        # Increased quartic regularization and chaotic dimension scaling
        result += 0.15 * np.sum(x**4)
        result *= (1.0 + 0.7 * np.log(self.dim + 1) * np.sin(0.5 * self.dim))
        
        # Normalize by dimension with chaotic adjustment
        result /= self.dim
        
        return result