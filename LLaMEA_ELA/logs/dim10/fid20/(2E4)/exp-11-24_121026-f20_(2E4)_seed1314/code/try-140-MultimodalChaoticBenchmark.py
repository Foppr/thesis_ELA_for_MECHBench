import numpy as np

class MultimodalChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] for stability
        x_norm = x / 5.0
        
        # Chaotic radial basis functions with quantum phase modulation
        rbfs = []
        for i in range(min(15, self.dim)):
            center = np.sin(i * np.pi / 8) if self.dim <= 15 else np.random.uniform(-1, 1)
            sigma = 0.3 + 0.4 * np.abs(np.sin(17 * center + np.cos(11 * center)))
            rbfs.append(np.exp(-np.sum((x_norm - center)**2) / (2 * sigma**2)) * 
                       np.sin(23 * center + np.cos(19 * center))**2)
        
        # Fractal-like chaotic coupling between dimensions
        fractal_coupling = 0.0
        for i in range(self.dim - 1):
            fractal_coupling += np.sin(25 * x_norm[i] + np.sin(31 * x_norm[i+1])) * \
                               np.cos(18 * x_norm[i+1] + np.sin(29 * x_norm[i]))
        
        # Quantum-inspired phase modulation with multiple frequencies
        phase_mod = 0.0
        for i in range(self.dim):
            phase_mod += np.sin(47 * x_norm[i] + np.sin(37 * x_norm[i]) + 
                               np.sin(23 * x_norm[i])) * \
                        np.cos(13 * x_norm[i] + np.cos(19 * x_norm[i]))
        
        # Polynomial chaos with fractional exponents
        poly_term = np.sum(np.abs(x_norm)**2.7 + 0.8 * np.abs(x_norm)**1.9 - 
                          0.4 * np.abs(x_norm)**3.1)
        
        # Self-similar chaotic structure with multiple scales
        self_similar = 0.0
        for scale in [2, 3, 5, 7]:
            self_similar += np.sum(np.sin(scale * x_norm + np.sin(scale**2 * x_norm))**2)
        
        # Add chaotic sinusoidal modulation with varying amplitudes and frequencies
        chaotic_mod = np.sum(np.sin(31 * x_norm + np.sin(17 * x_norm) * 
                                   np.cos(13 * x_norm)) * 
                            np.cos(23 * x_norm + np.sin(19 * x_norm) * 
                                  np.cos(11 * x_norm)))
        
        # Combine all components with dynamic weights
        return (0.8 * np.sum(rbfs) + 0.4 * phase_mod + 0.3 * poly_term + 
                0.25 * fractal_coupling + 0.15 * self_similar + 0.2 * chaotic_mod)