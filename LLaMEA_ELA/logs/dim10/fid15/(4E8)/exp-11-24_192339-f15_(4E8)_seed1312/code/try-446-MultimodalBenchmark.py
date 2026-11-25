import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Quantum harmonic oscillator parameters
        self.omega = np.random.rand(min(dim, 15)) * 2.0 + 1.0
        self.phi = np.random.rand(min(dim, 15)) * 2.0 * np.pi
        # Fractal potential well exponents
        self.fractal_exponents = np.random.rand(min(dim, 15)) * 3.0 + 1.0
        # Dynamic saddle-point modulation frequencies
        self.saddle_freqs = np.linspace(0.1, 1.5, min(dim, 10))
        # Stochastic resonance parameters
        self.noise_amp = np.random.rand(min(dim, 10)) * 0.5 + 0.1
        self.resonance_freq = np.random.rand(min(dim, 10)) * 0.8 + 0.2
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Quantum-inspired harmonic oscillators
        quantum = 0.0
        for i in range(self.dim):
            if i >= len(self.omega):
                break
            omega = self.omega[i % len(self.omega)]
            phi = self.phi[i % len(self.phi)]
            quantum += 0.5 * omega**2 * x[i]**2 + omega * x[i] * np.sin(phi)
        
        # Adaptive fractal potential wells
        fractal = 0.0
        for i in range(self.dim):
            if i >= len(self.fractal_exponents):
                break
            exp = self.fractal_exponents[i % len(self.fractal_exponents)]
            center = -4.0 + 8.0 * (i / max(1, self.dim - 1))
            distance = np.abs(x[i] - center)
            fractal += np.power(distance + 1e-8, exp) * np.cos(0.5 * x[i])
        
        # Dynamic saddle-point modulation
        saddle = 0.0
        for i in range(self.dim):
            if i >= len(self.saddle_freqs):
                break
            freq = self.saddle_freqs[i % len(self.saddle_freqs)]
            saddle += np.sin(freq * x[i]) * np.cos(freq * x[i]**2)
        
        # Enhanced stochastic resonance
        noise = 0.0
        for i in range(self.dim):
            if i >= len(self.noise_amp):
                break
            amp = self.noise_amp[i % len(self.noise_amp)]
            freq = self.resonance_freq[i % len(self.resonance_freq)]
            noise += amp * np.sin(freq * x[i] + np.random.rand() * 2.0 * np.pi)
        
        # Multi-scale complexity with varying curvature
        multiscale = 0.0
        for i in range(self.dim):
            scale_factor = 1.0 + 0.5 * np.sin(0.3 * i + self.dim * 0.1)
            curvature = 0.2 + 0.8 * np.cos(0.4 * x[i])
            multiscale += scale_factor * curvature * np.tanh(x[i]**3)
        
        # Emergent pattern formation with phase coupling
        patterns = 0.0
        for i in range(self.dim):
            if i >= len(self.omega):
                break
            omega_i = self.omega[i % len(self.omega)]
            phase_coupling = np.sin(omega_i * x[i] + 0.5 * np.cos(0.2 * i))
            patterns += phase_coupling * np.exp(-0.1 * x[i]**2)
        
        # Coupled sinusoidal transformations for increased non-separability
        coupled = 0.0
        for i in range(self.dim):
            if i < self.dim - 1:
                coupled += np.sin(0.5 * (x[i] + x[i+1])) * np.cos(0.3 * (x[i] - x[i+1]))
        
        # Combine all components with dynamic weighting
        dim_factor = 1.0 + 0.2 * np.log(self.dim + 1)
        return (0.25 * quantum + 0.20 * fractal + 
                0.25 * saddle + 0.15 * noise + 
                0.10 * multiscale + 0.08 * patterns + 
                0.07 * coupled) * dim_factor