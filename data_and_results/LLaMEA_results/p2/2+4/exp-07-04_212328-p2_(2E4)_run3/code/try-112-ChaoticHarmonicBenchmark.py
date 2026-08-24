import numpy as np

class ChaoticHarmonicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': -5.0, 'ub': 5.0})()
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Input dimension mismatch")
        
        # Base quadratic term with conditioning
        f = 0.5 * np.sum(x**2)
        
        # Time-varying harmonic potentials with chaotic modulation
        time_factor = np.sin(np.sum(x) * 0.1) * 0.5 + 0.75
        harmonic_sum = 0
        for i in range(self.dim):
            # Dynamic frequency modulation
            freq = 2.0 + 1.5 * np.sin(x[i] * 0.3 + time_factor * 0.5)
            # Amplitude modulation with chaotic pattern
            amp = 1.0 + 0.3 * np.sin(x[i] * 0.7 + time_factor * 0.3)
            harmonic_sum += amp * np.sin(freq * x[i])
        f += 2.0 * harmonic_sum * time_factor
        
        # Multi-scale periodic forcing with dynamic coupling
        forcing_sum = 0
        for i in range(self.dim):
            # Multiple periodic components with varying scales
            period1 = 2.0 + 0.5 * np.sin(x[i] * 0.2)
            period2 = 3.0 + 0.8 * np.cos(x[i] * 0.4)
            period3 = 1.5 + 0.4 * np.sin(x[i] * 0.6)
            
            forcing1 = np.sin(x[i] / period1)
            forcing2 = np.cos(x[i] / period2)
            forcing3 = np.sin(x[i] / period3)
            
            forcing_sum += forcing1 * forcing2 * forcing3
            
        f += 1.5 * forcing_sum
        
        # Dynamic coupling with time-varying weights
        coupling_sum = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Time-varying coupling strength
                coupling_strength = 0.5 + 0.5 * np.sin((x[i] + x[j]) * 0.2 + time_factor)
                coupling_sum += coupling_strength * np.sin(x[i] * x[j] * 0.5)
        f += 1.2 * coupling_sum
        
        # Rugged landscape with chaotic phase interactions
        phase_sum = 0
        for i in range(self.dim):
            # Chaotic phase interactions with dynamic amplitudes
            amp = 1.0 + 0.2 * np.sin(x[i] * 0.5 + time_factor * 0.3)
            phase_sum += amp * np.sin(x[i] + np.sin(x[i] * 0.8) + np.sin(x[i] * 0.3))
        f += 0.8 * np.sin(phase_sum * 2.0)
        
        # Multi-scale chaotic noise with varying intensity
        noise_sum = 0
        for i in range(self.dim):
            # Multi-frequency chaotic noise
            noise1 = np.sin(x[i] * 10.0 + np.sin(x[i] * 7.0))
            noise2 = np.cos(x[i] * 13.0 + np.cos(x[i] * 9.0))
            noise3 = np.sin(x[i] * 17.0 + np.sin(x[i] * 11.0))
            noise_sum += noise1 * noise2 * noise3
        f += 0.25 * noise_sum
        
        # Dynamic gradient modulation
        grad_mod = 0
        for i in range(self.dim):
            grad_mod += np.cos(x[i] * 0.3) * np.sin(x[i] * 0.7) * np.cos(x[i] * 0.9)
        f += 0.6 * grad_mod * time_factor
        
        # Nested harmonic minima with varying scales
        nested_sum = 0
        scales = [0.5, 1.0, 1.5, 2.0, 2.5]
        for s in scales:
            for i in range(self.dim):
                # Nested minima with different scales
                nested_sum += np.exp(-0.5 * (x[i] - s * np.sin(x[i] * 0.5))**2)
        f += 1.0 * nested_sum
        
        return f