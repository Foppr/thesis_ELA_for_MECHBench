import numpy as np

class ChaoticGradientSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic constants for fractal behavior
        self.c1 = np.random.rand(dim) * 2 - 1
        self.c2 = np.random.rand(dim) * 4 + 2
        self.c3 = np.random.rand(dim) * 0.8 + 0.2
        # Time-delay parameters for dynamic saddle points
        self.delay = np.random.rand(dim) * 0.5 + 0.1
        # Fractal scaling factors
        self.fractal_scale = np.random.rand(dim) * 3 + 1
        
    def f(self, x):
        x = np.array(x)
        
        # Base chaotic quadratic term with fractal scaling
        quad_term = 0.0
        for i in range(self.dim):
            quad_term += self.c1[i] * (x[i]**2) * self.fractal_scale[i]
            
        # Hyper-chaotic sine-wave modulation with time-delayed feedback
        chaotic_mod = 0.0
        for i in range(self.dim):
            # Time-delayed frequency modulation
            freq = 7.0 + 4.0 * np.sin(x[i] * 0.3) * np.cos(x[i-1] if i > 0 else x[-1] * 0.5)
            chaotic_mod += np.sin(freq * x[i]) * np.cos(freq * x[i]) * np.exp(-abs(x[i]))
            
        # Multi-scale fractal harmonic interaction with self-similar amplitudes
        harmonic_interaction = 0.0
        for i in range(self.dim):
            amp = 3.0 + 2.0 * np.sin(i * 0.5) * self.fractal_scale[i]
            for j in range(i+1, self.dim):
                amp_ij = amp * (1.0 + 0.7 * np.cos(i * j * 0.3)) * self.fractal_scale[j]
                harmonic_interaction += amp_ij * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
                
        # Saddle-point potential with time-delayed dynamics
        saddle_potential = 0.0
        for i in range(self.dim):
            # Delayed cubic and quartic terms
            delayed_x = x[i-1] if i > 0 else x[-1]
            saddle_potential += self.c2[i] * (x[i]**3 + 0.5 * delayed_x**3) + \
                               self.c3[i] * (x[i]**4 + 0.3 * delayed_x**4)
            
        # Implicit constraint penalty with adaptive threshold
        penalty = 0.0
        for i in range(self.dim):
            # Dynamic threshold based on dimension
            threshold = 5.0 + 0.5 * np.sin(i * 0.2)
            if abs(x[i]) > threshold:
                penalty += 150 * (abs(x[i]) - threshold)**2
                
        # Cross-dimensional coupling with fractal decay and multi-scale interactions
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = abs(x[i] - x[j])
                # Fractal exponential decay
                decay = np.exp(-dist * self.fractal_scale[i] * self.fractal_scale[j])
                cross_coupling += decay * np.sin(3 * (x[i] + x[j])) * np.cos(2 * (x[i] - x[j]))
                
        # Dynamic curvature modulation with fractal feedback
        curvature_mod = 0.0
        for i in range(self.dim):
            # Fractal-based curvature adjustment
            curvature_mod += (1.0 + 0.5 * np.sin(x[i]) * self.fractal_scale[i]) * x[i]**5
            
        # Multi-fractal harmonic term with recursive scaling
        fractal_harmonic = 0.0
        for k in range(3):  # Three levels of fractal recursion
            level_amp = 1.0 + 0.3 * np.sin(k * 0.7)
            for i in range(self.dim):
                for j in range(i+1, self.dim):
                    fractal_harmonic += level_amp * np.sin((i+j) * x[i] * x[j]) * np.cos((i-j) * x[i] * x[j])
        
        # Final function value with enhanced weighted components
        return 0.6 * quad_term + 0.8 * chaotic_mod + 0.7 * harmonic_interaction + \
               0.5 * saddle_potential + 0.9 * penalty + 0.4 * cross_coupling + \
               1.0 * curvature_mod + 0.5 * fractal_harmonic