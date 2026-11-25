import numpy as np

class AdaptiveTrigonometricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-pi, pi] range
        normalized_x = x * np.pi / 5.0
        
        # Base trigonometric oscillation with adaptive frequency
        base_oscillation = np.sum(np.sin(normalized_x) * np.cos(2 * normalized_x) + 
                                np.sin(3 * normalized_x) * np.cos(4 * normalized_x))
        
        # Adaptive frequency modulation based on input magnitude
        freq_modulation = np.sum((1 + 0.5 * np.sin(x)) * np.sin(5 * x) * np.cos(6 * x) + 
                               (1 + 0.3 * np.cos(x)) * np.sin(7 * x) * np.cos(8 * x))
        
        # Nested harmonic components with varying amplitudes
        nested_harmonics = 0.5 * np.sum(np.sin(10 * normalized_x) * np.cos(12 * normalized_x) + 
                                      np.sin(15 * normalized_x) * np.cos(18 * normalized_x) + 
                                      np.sin(20 * normalized_x) * np.cos(24 * normalized_x))
        
        # Discontinuous gradient components using step and ramp functions
        discontinuous = 0.3 * np.sum(np.heaviside(np.sin(normalized_x), 0.5) * np.cos(normalized_x) + 
                                   np.heaviside(np.cos(normalized_x), 0.5) * np.sin(normalized_x))
        
        # Multi-scale peak structures with varying heights
        peak_structures = 0.4 * np.sum(np.exp(-np.abs(x)) * np.sin(20 * x) + 
                                     np.exp(-np.abs(x)**2) * np.cos(15 * x) + 
                                     np.exp(-np.abs(x)**3) * np.sin(10 * x))
        
        # Self-similar pattern with recursive scaling
        self_similar = 0.35 * np.sum(np.sin(2**np.floor(np.log2(np.abs(x) + 1e-10))) * 
                                  np.cos(3**np.floor(np.log2(np.abs(x) + 1e-10))))
        
        # Chaotic phase modulation
        chaotic_phase = 0.25 * np.sum(np.sin(np.exp(x)) * np.cos(np.exp(-x)) + 
                                    np.sin(np.cos(x)) * np.cos(np.sin(x)))
        
        # Asymmetric oscillation with varying symmetry
        asymmetric = 0.3 * np.sum(np.sin(2 * x) * np.abs(np.cos(x)) + 
                               np.cos(3 * x) * np.abs(np.sin(x)))
        
        # Composite interaction term with cross-dimensional dependencies
        cross_interaction = 0.2 * np.sum(np.sin(x[:-1] + x[1:]) * np.cos(x[:-1] - x[1:]) + 
                                       np.sin(x[:-2] + x[2:]) * np.cos(x[:-2] - x[2:]))
        
        # Final composite function
        return 0.8 * (base_oscillation + freq_modulation + nested_harmonics + 
                     discontinuous + peak_structures + self_similar + chaotic_phase + 
                     asymmetric + cross_interaction)