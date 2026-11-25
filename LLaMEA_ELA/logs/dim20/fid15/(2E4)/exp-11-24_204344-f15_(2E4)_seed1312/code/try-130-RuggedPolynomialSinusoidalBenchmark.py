import numpy as np

class RuggedPolynomialSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        x = np.array(x)
        
        # Polynomial potential wells with varying degrees and positions
        polynomial = 0.0
        for i in range(self.dim):
            degree = 2 + int(i % 4)  # Degrees 2,3,4,5 repeating
            position = 1.5 + 0.5 * np.sin(i * 0.7)
            polynomial += (x[i] - position)**degree
        
        # Sinusoidal modulation with adaptive frequencies and amplitudes
        sinusoidal = 0.0
        for i in range(self.dim):
            freq = 3.0 + 2.0 * np.sin(i * 0.5)
            amp = 1.0 + 0.5 * np.cos(i * 0.3)
            phase = 0.5 * i + 0.2 * np.sin(i * 0.8)
            sinusoidal += amp * np.sin(freq * x[i] + phase) * np.cos(freq * x[i] + phase * 0.7)
        
        # Cross-dimensional interaction terms with modified coupling strengths
        cross_terms = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 0.7 + 0.3 * np.sin(i * j * 0.4)  # Increased coupling variability
                cross_terms += coupling * (x[i]**2 + x[j]**2) * np.sin(x[i] * x[j])
        
        # Adaptive noise layer with dynamic scaling
        noise = 0.0
        for i in range(self.dim):
            noise_scale = 0.1 + 0.05 * np.sin(i * 0.6)
            noise += noise_scale * np.random.normal(0, 1) * (1.0 + 0.3 * np.cos(x[i]))
        
        # Multi-scale harmonic components with modified frequencies and amplitudes
        harmonic = 0.0
        for i in range(self.dim):
            freq = 1.5 + 0.5 * np.sin(i * 0.4)  # Increased frequency variability
            amp = 2.0 + 1.0 * np.cos(i * 0.3)
            harmonic += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.5)
        
        # Asymmetric exponential decay terms with position-dependent parameters
        exp_decay = 0.0
        for i in range(self.dim):
            decay_rate = 0.3 + 0.2 * np.sin(i * 0.8)
            offset = 0.5 * np.cos(i * 0.6)
            exp_decay += np.exp(-decay_rate * (x[i] - offset)**2) * np.sin(4 * x[i])
        
        # Combined landscape with modified weights
        return (0.8 * polynomial + 0.6 * sinusoidal + 0.7 * cross_terms + 
                0.5 * noise + 1.0 * harmonic + 0.4 * exp_decay)