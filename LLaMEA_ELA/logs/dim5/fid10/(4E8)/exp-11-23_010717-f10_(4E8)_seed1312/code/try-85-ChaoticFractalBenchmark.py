import numpy as np

class ChaoticFractalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-5, 5] if not already
        x = np.clip(x, -5.0, 5.0)
        
        # Nested fractal basin terms with varying scales and depths
        basin = 0.0
        scales = [0.1, 0.05, 0.025]
        for i, scale in enumerate(scales):
            basin += scale * np.sum(np.sin((i+1) * x)**2 + np.cos((i+1) * x)**2)
        
        # Multi-scale sinusoidal grid with varying frequencies and amplitudes
        grid = 0.0
        for i in range(self.dim):
            freqs = [1.0, 2.5, 4.0, 6.0]
            amps = [1.5, 0.8, 0.4, 0.2]
            for freq, amp in zip(freqs, amps):
                grid += amp * np.sin(freq * x[i]) * np.cos(freq * x[i])
        
        # Cross-dimensional coupling with chaotic interaction patterns
        cross = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Chaotic coupling with varying interaction strengths
                strength = 0.5 + 0.5 * np.sin(0.5 * (i + j))
                cross += strength * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
        
        # Adaptive noise component with fractal characteristics and dynamic modulation
        noise = 0.0
        for i in range(self.dim):
            # Dynamic noise amplitude based on position
            amp = 0.1 * (1.0 + 0.5 * np.sin(3.0 * x[i]))
            noise += amp * np.sin(10.0 * x[i]) * np.cos(8.0 * x[i])
        
        # Higher-order polynomial terms with chaotic coefficients
        poly = 0.0
        coeffs = [0.05, 0.02, 0.01]
        for i, coeff in enumerate(coeffs):
            power = i + 3
            poly += coeff * np.sum(x**power)
        
        # Chaotic sine-cosine combination with dynamic phase shifts
        chaotic = 0.0
        phases = [np.pi/4, np.pi/2, 3*np.pi/4]
        for i, phase in enumerate(phases):
            chaotic += 0.3 * np.sin(2.0 * x[i] + phase) * np.cos(1.5 * x[i] + phase)
        
        # Combined fitness function with dynamic scaling
        total = basin + grid + cross + noise + poly + chaotic
        
        # Add a global scaling factor to ensure proper fitness range
        return 0.1 * total + 0.01 * np.sum(x**6)