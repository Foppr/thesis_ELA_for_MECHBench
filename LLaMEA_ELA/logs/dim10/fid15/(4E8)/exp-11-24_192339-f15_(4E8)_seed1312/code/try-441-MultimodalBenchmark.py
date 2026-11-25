import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute quantum harmonic oscillator parameters
        self.omega = np.random.rand(min(dim, 20)) * 3.0 + 1.0
        self.phi = np.random.rand(min(dim, 20)) * 2.0 * np.pi
        # Fractal potential well exponents
        self.fractal_exponents = np.random.rand(min(dim, 20)) * 4.0 + 1.0
        # Dynamic saddle-point modulation
        self.saddle_freqs = np.linspace(0.05, 2.0, min(dim, 15))
        # Stochastic resonance parameters
        self.noise_amp = np.random.rand(min(dim, 15)) * 0.7 + 0.1
        self.resonance_freq = np.random.rand(min(dim, 15)) * 1.0 + 0.1
        # Additional chaotic components
        self.chaos_params = np.random.rand(min(dim, 15)) * 2.0 + 0.5
        self.memory_decay = np.random.rand(min(dim, 15)) * 0.3 + 0.1
        
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
        
        # Chaotic enhancement and memory effects
        chaos = 0.0
        for i in range(self.dim):
            if i >= len(self.chaos_params):
                break
            chaos_param = self.chaos_params[i % len(self.chaos_params)]
            memory = self.memory_decay[i % len(self.memory_decay)]
            chaos += chaos_param * np.sin(x[i] * 1.5 + np.cos(x[i-1] if i > 0 else x[-1]) * memory)
        
        # Combine all components with dynamic weighting
        dim_factor = 1.0 + 0.3 * np.log(self.dim + 1)
        return (0.20 * quantum + 0.25 * fractal + 
                0.20 * saddle + 0.10 * noise + 
                0.10 * multiscale + 0.10 * patterns + 
                0.05 * chaos) * dim_factor