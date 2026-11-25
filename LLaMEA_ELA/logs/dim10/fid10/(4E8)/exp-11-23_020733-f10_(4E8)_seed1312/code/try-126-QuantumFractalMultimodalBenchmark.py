import numpy as np

class QuantumFractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute fractal parameters for different dimensions
        self.fractal_dims = [0.5 + 0.3 * np.sin(i * np.pi / (self.dim + 1)) for i in range(self.dim)]
        self.oscillator_freqs = [1.2 + 0.8 * np.cos(i * np.pi / (self.dim + 2)) for i in range(self.dim)]
        self.gating_strengths = [1.5 + 0.5 * np.sin(i * np.pi / (self.dim + 3)) for i in range(self.dim)]
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quantum harmonic oscillator term
        result = 0.1 * np.sum(x**2)
        
        # Quantum-inspired harmonic oscillators with dimensionally varying frequencies
        for i in range(self.dim):
            freq = self.oscillator_freqs[i]
            result += 2.0 * (x[i]**2) * np.sin(freq * x[i])**2 + 1.5 * np.cos(freq * x[i])**2
        
        # Fractional Brownian motion fractal components with varying Hurst parameters
        for i in range(self.dim):
            hurst = self.fractal_dims[i]
            fractal_term = 0.0
            for k in range(1, min(6, self.dim + 1)):
                scale = 2.0**(-k * hurst)
                phase = np.sin(k * x[i] + i * np.pi / (self.dim + 1))
                fractal_term += scale * np.sin(k * x[i]) * phase
            result += 1.2 * fractal_term
        
        # Adaptive neural network-like gating with multi-scale interactions
        for i in range(self.dim):
            gating = self.gating_strengths[i]
            # Multi-scale gating with different interaction radii
            gate_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    dist = abs(x[i] - x[j])
                    radius = 1.0 + 0.5 * np.sin(i * j * np.pi / (self.dim + 1))
                    gate_sum += gating * np.exp(-dist**2 / (2 * radius**2)) * np.tanh(x[j])
            result += 0.8 * gate_sum
        
        # Multi-scale periodic potential with quantum-like tunneling effects
        for i in range(self.dim):
            scale = 1.0 + 0.5 * np.cos(i * np.pi / (self.dim + 2))
            result += 3.0 * np.sin(scale * x[i])**4 + 2.0 * np.cos(scale * x[i])**3
        
        # Cross-dimensional coupling with fractal scaling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt((x[i] - x[j])**2)
                fractal_coupling = 0.5 * np.sin(dist)**2 + 0.3 * np.cos(dist)**2
                result += fractal_coupling * (1.0 + 0.4 * np.sin(i + j))
        
        # Boundary-induced quantum tunneling effect
        boundary_effect = 0.0
        for i in range(self.dim):
            if abs(x[i]) > 4.0:
                penalty = 5.0 * (abs(x[i]) - 4.0)**2 * np.exp(-abs(x[i])**2 / 50.0)
                boundary_effect += penalty
        result += boundary_effect
        
        # Global quantum phase modulation
        global_phase = np.sin(np.sum(x) * np.pi / (self.dim + 1)) * np.cos(np.sum(x) * np.pi / (self.dim + 2))
        result *= (1.0 + 0.3 * global_phase)
        
        return result