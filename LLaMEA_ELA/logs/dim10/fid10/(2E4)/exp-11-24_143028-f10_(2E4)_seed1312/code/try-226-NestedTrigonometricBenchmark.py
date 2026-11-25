import numpy as np

class NestedTrigonometricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute adaptive frequencies and coupling coefficients
        self.frequencies = np.linspace(1.0, 20.0, min(20, dim))
        self.coupling_coeffs = np.random.rand(min(20, dim)) * 1.5 + 0.5
        self.fractal_scale = np.logspace(0, 2.8, min(15, dim))
        # Add stochastic components for increased diversity
        self.stochastic_phase = np.random.rand(dim) * 2 * np.pi
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced nested trigonometric oscillation component with stochastic modulation
        trig_term = 0.0
        for i in range(self.dim):
            freq = self.frequencies[i] * (1 + 0.5 * np.sin(0.7 * x[i] + self.stochastic_phase[i]))
            trig_term += (np.sin(freq * x[i]) + 0.7 * np.cos(2 * freq * x[i]) + 
                         0.4 * np.sin(3 * freq * x[i]) + 0.2 * np.cos(5 * freq * x[i]))**2
        
        # Enhanced polynomial coupling with stochastic coefficients and higher-order terms
        poly_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Stochastic coupling coefficient
                coeff = self.coupling_coeffs[i] * self.coupling_coeffs[j] * (1 + 0.3 * np.sin(self.stochastic_phase[i] + self.stochastic_phase[j]))
                poly_coupling += coeff * (x[i]**4 + x[j]**4 + x[i]**2 * x[j]**2) * np.sin(x[i] * x[j]) * np.cos(0.6 * x[i] + 0.4 * x[j]) * np.exp(-0.15 * abs(x[i] - x[j]))
        
        # Enhanced fractal-like boundary effects with stochastic penalties
        boundary_effect = 0.0
        for i in range(self.dim):
            if x[i] < -4.7:
                penalty = 2.5 * (np.exp(-0.3 * (x[i] + 4.7)**2) + 0.5 * np.sin(15 * x[i]))
                boundary_effect += penalty * (1 + 0.2 * np.sin(self.stochastic_phase[i]))
            elif x[i] > 4.7:
                penalty = 3.0 * (np.exp(-0.25 * (x[i] - 4.7)**2) + 0.4 * np.cos(12 * x[i]))
                boundary_effect += penalty * (1 + 0.2 * np.cos(self.stochastic_phase[i]))
        
        # Multi-scale harmonic interference with stochastic amplitudes and phases
        interference_term = 0.0
        for i in range(self.dim):
            for k in range(1, min(12, self.dim+1)):
                # Stochastic amplitude and phase
                amp = 1.5 + 0.8 * np.sin(k * x[i] + self.stochastic_phase[i]) * np.cos(i * 0.6)
                phase = 0.4 * np.sin(i * 0.5 + self.stochastic_phase[i]) * k + 0.2 * np.cos(i * 0.3 + self.stochastic_phase[i])
                interference_term += amp * np.sin(k * x[i] + phase) * np.cos(k**1.5 * x[i]) * np.exp(-0.12 * abs(x[i]))
        
        # Enhanced fractal modulation with stochastic scaling
        fractal_mod = 0.0
        for i in range(self.dim):
            scale = self.fractal_scale[i % len(self.fractal_scale)] * (1 + 0.3 * np.sin(self.stochastic_phase[i]))
            fractal_mod += scale * np.sin(scale * x[i]) * np.cos(scale * x[i]**2) + 0.6 * np.sin(0.6 * scale * x[i]**3)
        
        # Combine all components with adjusted weights for better balance
        result = 0.9 * trig_term + 0.7 * poly_coupling + 0.6 * boundary_effect + \
                 0.8 * interference_term + 0.5 * fractal_mod
        
        return result