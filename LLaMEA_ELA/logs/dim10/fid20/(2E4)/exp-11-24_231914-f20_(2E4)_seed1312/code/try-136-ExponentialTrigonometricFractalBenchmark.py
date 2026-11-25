import numpy as np

class ExponentialTrigonometricFractalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize parameters for exponential-trigonometric fractal components
        self.exp_rates = np.random.uniform(0.1, 2.0, size=dim)
        self.trig_freqs = np.random.uniform(2.0, 15.0, size=dim)
        self.fractal_dims = np.random.uniform(0.5, 2.5, size=dim)
        self.stochastic_amps = np.random.uniform(0.5, 3.0, size=dim)
        self.coupling_strengths = np.random.uniform(0.1, 1.5, size=dim)
        
    def f(self, x):
        # Scale input to [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Exponential-trigonometric fractal component
        exp_trig = 0.0
        for i in range(self.dim):
            rate = self.exp_rates[i]
            freq = self.trig_freqs[i]
            exp_trig += np.exp(rate * np.abs(x[i])) * np.sin(freq * x[i]) * np.cos(freq * x[i])
            
        # Fractal-like geometric transformation with varying dimensions
        fractal_geom = 0.0
        for i in range(self.dim):
            dim_factor = self.fractal_dims[i]
            fractal_geom += (np.abs(x[i])**dim_factor) * np.sin(dim_factor * np.log(np.abs(x[i]) + 1e-8))
            
        # Multi-scale coupling with exponential decay
        coupling = 0.0
        for i in range(self.dim - 1):
            strength = self.coupling_strengths[i]
            coupling += strength * np.exp(-0.5 * (x[i] - x[i+1])**2) * (x[i]**2 + x[i+1]**2)
            
        # Stochastic perturbation with dynamic amplitude
        stochastic = 0.0
        for i in range(self.dim):
            amp = self.stochastic_amps[i]
            stochastic += amp * np.sin(x[i] + np.random.rand() * np.pi) * np.exp(-0.1 * x[i]**2)
            
        # High-frequency fractal interference pattern
        high_freq_pattern = 0.0
        for i in range(self.dim):
            freq = self.trig_freqs[i] * 5
            high_freq_pattern += np.sin(freq * x[i]) * np.cos(freq * x[i]) * np.tan(0.1 * x[i])
            
        # Combined landscape with dynamic weights
        return (1.5 * exp_trig + 
                1.3 * fractal_geom + 
                0.8 * coupling + 
                1.4 * stochastic + 
                1.1 * high_freq_pattern)