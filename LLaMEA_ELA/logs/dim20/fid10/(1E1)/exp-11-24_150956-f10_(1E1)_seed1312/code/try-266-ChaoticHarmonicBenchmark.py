import numpy as np

class ChaoticHarmonicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute constants for chaos generation
        self.r = 3.9  # Logistic map parameter for chaos
        self.chaos_sequence = self._generate_chaos_sequence()
        
    def _generate_chaos_sequence(self):
        # Generate chaotic sequence using logistic map
        seq = np.zeros(self.dim)
        x = 0.5
        for i in range(self.dim):
            x = self.r * x * (1 - x)
            seq[i] = x
        return seq
    
    def f(self, x):
        # Scale input to [-1, 1]
        x_scaled = x / 5.0
        
        # Chaotic component using logistic map dynamics
        chaotic = np.sum(self.chaos_sequence * np.sin(20.0 * x_scaled) * 
                        np.cos(15.0 * x_scaled) + 
                        np.sin(30.0 * x_scaled**2) * np.cos(25.0 * x_scaled**2))
        
        # Spherical harmonics component in higher dimensions
        sph_harm = 0.0
        if self.dim >= 2:
            # Create 2D spherical harmonic-like terms
            r = np.sqrt(x_scaled[:-1]**2 + x_scaled[1:]**2)
            theta = np.arctan2(x_scaled[1:], x_scaled[:-1])
            sph_harm = np.sum(r * np.sin(5.0 * theta) * np.cos(3.0 * theta))
        
        # Quaternion-inspired rotation terms
        rot_terms = 0.0
        if self.dim >= 4:
            for i in range(0, self.dim - 3, 4):
                # Simple quaternion-like interaction
                q1 = x_scaled[i] * x_scaled[i+1]
                q2 = x_scaled[i+2] * x_scaled[i+3]
                rot_terms += np.sin(q1 + q2) * np.cos(q1 - q2)
        
        # Multi-scale exponential modulation with sinusoidal interference
        exp_mod = np.sum(np.exp(-2.0 * np.abs(x_scaled)) * 
                        (1.0 + 0.5 * np.sin(10.0 * x_scaled) + 
                         0.3 * np.cos(15.0 * x_scaled)))
        
        # Cross-dimensional coupling with cubic interactions
        cross_coupling = np.sum((x_scaled[:-2]**3 + x_scaled[2:]**3) * 
                              np.sin(4.0 * (x_scaled[:-2] - x_scaled[2:])) + 
                              (x_scaled[:-1]**2 * x_scaled[1:] + 
                               x_scaled[:-1] * x_scaled[1:]**2) * 
                              np.cos(3.0 * (x_scaled[:-1] + x_scaled[1:])))
        
        # Final combined function
        return 0.4 * chaotic + 0.25 * sph_harm + 0.15 * rot_terms + \
               0.1 * exp_mod + 0.1 * cross_coupling + 2.1