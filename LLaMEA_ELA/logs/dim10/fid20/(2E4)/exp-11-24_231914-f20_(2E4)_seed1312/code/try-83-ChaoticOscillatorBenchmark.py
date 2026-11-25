import numpy as np

class ChaoticOscillatorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute dynamic phase shift parameters with fractional scaling
        self.phase_shifts = np.linspace(0.1, 2.0, min(dim, 10))
        # Fractional order parameters for chaotic behavior
        self.frac_orders = np.linspace(0.3, 1.7, min(dim, 15))
        
    def f(self, x):
        # Scale input to [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base conditioning term with fractional scaling
        base = np.sum(x**2) / self.dim
        
        # Fractional-order nested trigonometric oscillators
        oscillator = 0.0
        for i in range(self.dim):
            freq = 1.0 + 0.5 * (i + 1) / self.dim
            phase = self.phase_shifts[i % len(self.phase_shifts)]
            frac_order = self.frac_orders[i % len(self.frac_orders)]
            
            # Fractional-order oscillation with enhanced complexity
            oscillator += (
                np.sin(freq * x[i] + phase) ** frac_order * 
                np.cos(freq**1.5 * x[i] + phase**2) ** (frac_order * 0.7) *
                np.sin(freq**2 * x[i] + phase**3) ** (frac_order * 0.5) *
                np.exp(-0.1 * np.abs(x[i]))
            )
        
        # Dynamic coupling with variable strength and fractional interaction
        coupling = 0.0
        for i in range(self.dim - 1):
            strength = 1.0 / (i + 1)
            frac_coupling = 0.5 + 0.5 * np.sin(i * 0.3)  # Dynamic fractional coupling
            
            coupling += strength * (
                np.sin(x[i] + x[i+1]) ** frac_coupling * 
                np.cos(x[i] - x[i+1]) ** (frac_coupling * 0.8) *
                np.tan(0.5 * (x[i]**2 + x[i+1]**2)) ** frac_coupling *
                np.exp(-0.2 * (x[i]**2 + x[i+1]**2))
            )
        
        # Multi-scale chaotic modulation with fractional decay
        chaotic_mod = 0.0
        for i in range(self.dim):
            scales = [0.5, 1.0, 2.0, 3.0]
            mod = 0.0
            for scale in scales:
                frac_scale = 0.5 + 0.5 * np.cos(i * 0.2)  # Dynamic fractional modulation
                mod += np.sin(scale * x[i]) ** frac_scale * np.cos(scale**1.2 * x[i]) ** (frac_scale * 0.6) * np.exp(-scale * np.abs(x[i]))
            chaotic_mod += mod * np.exp(-0.15 * (i + 1))
        
        # Adaptive phase rotation with fractional weights
        phase_rotation = 0.0
        for i in range(self.dim):
            frac_weight = 0.3 + 0.7 * np.sin(i * 0.4)  # Dynamic fractional weight
            rot = (np.sin(x[i]) * np.cos(x[i] * (i + 1))) ** frac_weight * np.exp(-0.05 * x[i]**2)
            phase_rotation += rot * (i + 1) / self.dim
        
        # Combine all components with optimized weights for better fitness
        return base + 2.5 * oscillator + 1.8 * coupling + 1.6 * chaotic_mod + 0.9 * phase_rotation