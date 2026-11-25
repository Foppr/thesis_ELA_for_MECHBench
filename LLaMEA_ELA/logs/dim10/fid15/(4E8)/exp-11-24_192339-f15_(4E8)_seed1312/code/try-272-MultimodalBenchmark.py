import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Quantum harmonic oscillator interactions with 3D chaotic logistic map modulation
        quantum_interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # 3D logistic map modulation for phase shift
                log_a = 4.0 * np.sin(x[i]) * np.cos(x[j])
                log_b = 4.0 * np.cos(x[i]) * np.sin(x[j])
                log_c = 4.0 * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
                logistic_phase = (log_a * (1 - log_a**2) + 
                                 log_b * (1 - log_b**2) + 
                                 log_c * (1 - log_c**2)) / 3.0
                coupling = np.sin(x[i] * x[j] * (1 + 0.2 * np.sin(x[i]**2 + x[j]**2) + 
                                                0.1 * logistic_phase)) * \
                          np.cos(0.5 * (x[i] - x[j])**2) * \
                          np.exp(-0.05 * (x[i]**2 + x[j]**2))
                quantum_interaction += coupling
        
        # Dynamic saddle point injection with fractal Gaussian peaks
        fractal_gaussians = 0
        for i in range(self.dim):
            peak_height = 1.5 + 0.8 * np.sin(0.4 * x[i] + self.dim * 0.1)
            peak_width = 1.0 + 0.3 * np.cos(0.6 * x[i])
            # Add saddle point term
            saddle_term = 0.2 * np.sin(2 * x[i]) * np.cos(2 * x[i])
            gaussian_term = (peak_height + saddle_term) * np.exp(-0.5 * (x[i] / peak_width)**2)
            fractal_gaussians += gaussian_term
        
        # Recursive sine-cosine fractal gradient with dynamic scaling
        fractal_modulation = 0
        for i in range(self.dim):
            scale_factor = 1.0 + 0.5 * np.sin(0.3 * x[i] + self.dim * 0.2)
            # Add recursive pattern for increased complexity
            recursive_term = np.sin(scale_factor * x[i]) * \
                           np.cos(scale_factor * x[i]**2) * \
                           np.sin(scale_factor * x[i]**3) * \
                           np.cos(scale_factor * x[i]**4) * \
                           np.exp(-0.1 * x[i]**2)
            fractal_modulation += recursive_term
        
        # Multi-scale multimodal structure with time-varying frequencies and chaotic modulation
        multimodal = 0
        for i in range(self.dim):
            freq1 = 3.0 + 2.0 * np.sin(0.1 * x[i] + self.dim * 0.15) + 0.5 * np.sin(0.05 * x[i]**2)
            freq2 = 4.0 + 3.0 * np.cos(0.2 * x[i]**2 + self.dim * 0.1) + 0.3 * np.cos(0.1 * x[i])
            freq3 = 2.5 + 1.5 * np.sin(0.3 * x[i] * self.dim) + 0.4 * np.sin(0.08 * x[i]**3)
            multimodal += np.sin(freq1 * x[i]) * \
                         np.cos(freq2 * x[i]) * \
                         np.tanh(freq3 * x[i]) * \
                         np.exp(-0.05 * x[i]**2)
        
        # Cross-dimensional coupling with hyperbolic and exponential interactions, including chaotic modulation
        cross_interaction = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):
                dist = np.sqrt((x[i] - x[j])**2 + 1e-6)
                # Add chaotic modulation to coupling
                chaos_mod = 0.1 * np.sin(3 * (x[i] + x[j]) * np.cos(x[i] - x[j]))
                coupling = (np.tanh(dist * (1 + 0.3 * np.sin(x[i] + x[j]) + chaos_mod)) * 
                           np.exp(-0.2 * dist**2) * 
                           np.cos(0.5 * dist) * 
                           np.sin(0.2 * dist))
                cross_interaction += coupling
        
        # Asymmetric conditioning with dynamic dimensionality-dependent scaling and chaotic component
        conditioning = 1.0 + 0.2 * np.sin(self.dim * 0.4) + 0.15 * np.cos(self.dim * 0.3) + \
                      0.08 * np.sin(self.dim * 0.6) + 0.05 * np.sin(0.1 * self.dim**2)
        
        # Combine all components with optimized weights
        return conditioning * (0.2 * quantum_interaction + 0.35 * fractal_gaussians + 
                              0.25 * fractal_modulation + 0.15 * multimodal + 0.05 * cross_interaction)