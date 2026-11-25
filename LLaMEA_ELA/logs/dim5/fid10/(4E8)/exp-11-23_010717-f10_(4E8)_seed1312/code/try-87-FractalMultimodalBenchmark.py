import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-5, 5] if not already
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with variable scaling
        base = 0.1 * np.sum(x**2)
        
        # Enhanced fractal-like basin structure using logarithmic scaling with higher penalty
        fractal_basin = 0.0
        for i in range(self.dim):
            # Increased logarithmic penalty that intensifies near boundaries
            log_penalty = 1.5 + 2.0 * np.log(1.0 + np.abs(x[i]))
            fractal_basin += log_penalty * (x[i]**2)
        
        # Modified chaotic sine-wave interactions with more complex frequency modulation
        chaotic_interaction = 0.0
        for i in range(self.dim):
            # Use more complex sine-cosine combinations with multi-frequency modulation
            freq_mod1 = 1.0 + 0.8 * np.sin(0.5 * x[i])
            freq_mod2 = 1.0 + 0.6 * np.cos(0.3 * x[i])
            chaotic_interaction += 3.0 * np.sin(freq_mod1 * x[i]) * np.cos(freq_mod2 * x[i] * 0.7) + \
                                 1.5 * np.sin(freq_mod1 * x[i] * 1.2) * np.cos(freq_mod2 * x[i] * 1.4)
        
        # Enhanced cross-dimensional coupling with more complex nonlinear interactions
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Stronger nonlinear interaction with exponential and trigonometric scaling
                exp_interaction = np.exp(-0.2 * (x[i]**2 + x[j]**2))
                cross_coupling += 1.0 * exp_interaction * np.sin(x[i] * x[j]) * np.cos(x[i] + x[j]) * \
                                  (1.0 + 0.5 * np.sin(0.5 * (x[i] + x[j])))
        
        # Additional noise components to increase irregularity
        noise_component = 0.0
        for i in range(self.dim):
            noise_component += 0.3 * np.random.uniform(-1, 1) * np.sin(2.0 * x[i])
        
        # Step-function like penalty for non-smooth behavior with enhanced variation
        step_penalty = 0.0
        for i in range(self.dim):
            step_penalty += 0.8 * np.floor(3.0 + np.sin(x[i])) * (x[i]**2)
        
        # Additional high-frequency oscillation to increase condition number and challenge optimization
        high_freq = 0.0
        for i in range(self.dim):
            high_freq += 2.0 * np.sin(15.0 * x[i]) * np.cos(12.0 * x[i])
        
        return base + fractal_basin + chaotic_interaction + cross_coupling + noise_component + step_penalty + high_freq