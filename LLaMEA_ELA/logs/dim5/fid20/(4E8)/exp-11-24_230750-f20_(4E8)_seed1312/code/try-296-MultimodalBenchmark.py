import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Periodic cosine oscillation component with varying frequencies
        cos_oscillation = 0.0
        for i in range(self.dim):
            freq = 1.0 + 0.5 * np.sin(i)
            cos_oscillation += np.cos(freq * x[i]) ** 2 + 0.3 * np.cos(2 * freq * x[i])
        
        # Adaptive parabolic valleys with dynamic centers and widths
        parabolic_valleys = 0.0
        for i in range(self.dim):
            center = 2.0 * np.sin(0.5 * x[i])
            width = 1.0 + 0.5 * np.cos(x[i])
            parabolic_valleys += (x[i] - center) ** 2 / (width ** 2 + 0.1)
        
        # Cross-dimensional cubic couplings with varying interaction strengths
        cubic_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                strength = 0.5 + 0.5 * np.sin(0.5 * (x[i] + x[j]))
                cubic_coupling += strength * (x[i] ** 3 + x[j] ** 3) * np.exp(-0.1 * ((x[i] - x[j]) ** 2))
        
        # Multi-scale periodic peaks with varying amplitudes and phases
        periodic_peaks = 0.0
        for i in range(self.dim):
            amplitude = 1.0 + 0.5 * np.sin(2 * x[i])
            phase = 0.5 * np.cos(x[i])
            periodic_peaks += amplitude * np.sin(3 * x[i] + phase) ** 2
        
        # Gradient deception through polynomial-modulated sinusoidal components
        deception = 0.0
        for i in range(self.dim):
            poly_mod = 1.0 + 0.3 * x[i] ** 4
            sin_mod = np.sin(2 * x[i]) + 0.2 * np.cos(3 * x[i])
            deception += poly_mod * sin_mod * (1.0 + 0.1 * np.sin(x[i]))
        
        # Combine all components with carefully tuned weights for optimal challenge
        return 0.25 * cos_oscillation + 0.20 * parabolic_valleys + 0.20 * cubic_coupling + 0.20 * periodic_peaks + 0.15 * deception