import numpy as np

class FractalPhaseTransitionBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute fractal scaling factors
        self.fractal_factors = [np.sin(i * 0.3) + 1.5 for i in range(dim)]
    
    def f(self, x):
        x = np.array(x)
        
        # Base quadratic term with adaptive weights
        base_quad = 0.0
        for i in range(self.dim):
            weight = 1.0 + 0.5 * np.sin(i * 0.4)
            base_quad += weight * x[i]**2
        
        # Fractal-like harmonic components with diminishing amplitudes
        fractal_harmonic = 0.0
        for i in range(self.dim):
            amp = 0.1 * (1.0 / (i + 1)) * self.fractal_factors[i]
            freq = 2**(i % 5 + 1)
            fractal_harmonic += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.5)
        
        # Dynamic coupling with phase transitions
        dynamic_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Phase transition based on distance between variables
                dist = np.abs(x[i] - x[j])
                transition = 1.0 if dist < 1.0 else 0.2
                coupling_strength = 0.5 * transition * (i + j) % 3
                dynamic_coupling += coupling_strength * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
        
        # Embedded fractal potential wells with varying depths
        fractal_wells = 0.0
        for i in range(self.dim):
            depth = 1.0 + 0.5 * np.sin(i * 0.7)
            well_pos = 2.0 * np.sin(i * 0.6)
            fractal_wells += depth * (x[i] - well_pos)**4
        
        # Multi-scale oscillatory behavior with frequency modulation
        oscillatory = 0.0
        for i in range(self.dim):
            freq_mod = 1.0 + 0.3 * np.cos(i * 0.5)
            oscillatory += np.sin(freq_mod * x[i]) * np.cos(freq_mod * x[i] * 0.8) * np.exp(-0.1 * x[i]**2)
        
        # Asymmetric sigmoidal transformation with adaptive steepness
        sigmoid_transform = 0.0
        for i in range(self.dim):
            steepness = 1.0 + 0.4 * np.sin(i * 0.3)
            sigmoid_transform += np.log(1.0 + np.exp(steepness * x[i]))
        
        # Cross-dimensional exponential interaction with threshold behavior
        exp_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                diff = x[i] - x[j]
                if abs(diff) < 0.5:
                    exp_interaction += np.exp(-0.5 * diff**2) * np.sin(3 * (x[i] + x[j]))
                else:
                    exp_interaction += 0.1 * np.exp(-diff**2) * np.cos(2 * (x[i] - x[j]))
        
        # Final landscape with weighted components
        return 0.4 * base_quad + 0.6 * fractal_harmonic + 0.5 * dynamic_coupling + \
               0.7 * fractal_wells + 0.3 * oscillatory + 0.8 * sigmoid_transform + 0.4 * exp_interaction