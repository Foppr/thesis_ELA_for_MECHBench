import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute quantum harmonic oscillator parameters
        self.omega = np.linspace(0.1, 3.0, min(dim, 15))
        self.phase = np.linspace(0.0, 2*np.pi, min(dim, 15))
        # Precompute fractal potential well exponents
        self.fractal_exponents = np.random.rand(min(dim, 15)) * 2.0 + 1.0
        # Dynamic saddle-point modulation
        self.saddle_mod = np.random.rand(min(dim, 15)) * 0.5 + 0.25
        # Enhanced stochastic resonance parameters
        self.noise_amplitude = 0.1 + 0.2 * np.random.rand(min(dim, 15))
        self.resonance_freq = np.linspace(0.5, 2.5, min(dim, 15))
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Quantum-inspired harmonic oscillators
        quantum = 0.0
        for i in range(self.dim):
            if i >= len(self.omega):
                break
            omega = self.omega[i % len(self.omega)]
            phase = self.phase[i % len(self.phase)]
            quantum += 0.5 * omega**2 * x[i]**2 + omega * x[i] * np.sin(phase)
        
        # Adaptive fractal potential wells
        fractal = 0.0
        for i in range(self.dim):
            if i >= len(self.fractal_exponents):
                break
            exp = self.fractal_exponents[i % len(self.fractal_exponents)]
            fractal += np.abs(x[i])**exp
        
        # Dynamic saddle-point modulation
        saddle = 0.0
        for i in range(self.dim):
            if i >= len(self.saddle_mod):
                break
            mod = self.saddle_mod[i % len(self.saddle_mod)]
            saddle += x[i]**2 * np.cos(mod * x[i])
        
        # Enhanced stochastic resonance
        noise = 0.0
        for i in range(self.dim):
            if i >= len(self.noise_amplitude):
                break
            amp = self.noise_amplitude[i % len(self.noise_amplitude)]
            freq = self.resonance_freq[i % len(self.resonance_freq)]
            noise += amp * np.sin(freq * x[i] + np.random.rand() * 2 * np.pi)
        
        # Multi-scale complexity with exponential coupling
        multiscale = 0.0
        for i in range(self.dim):
            scale_factor = 1.0 + 0.5 * np.sin(0.3 * i + self.dim * 0.15)
            multiscale += scale_factor * np.exp(-0.1 * x[i]**2) * np.cos(2.0 * x[i])
        
        # Emergent pattern formation with cross-term interactions
        pattern = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                if i >= len(self.omega) or j >= len(self.omega):
                    break
                coupling = np.sin(self.omega[i % len(self.omega)] * x[j] + 
                                 self.omega[j % len(self.omega)] * x[i])
                pattern += coupling * (x[i]**2 + x[j]**2)
        
        # Combine all components with dynamic weighting based on dimension
        dim_factor = 1.0 + 0.2 * np.log(self.dim + 1)
        return (0.25 * quantum + 0.20 * fractal + 
                0.25 * saddle + 0.15 * noise + 
                0.10 * multiscale + 0.05 * pattern) * dim_factor